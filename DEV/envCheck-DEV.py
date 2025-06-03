##############
#  elimPawn  #
# envCheckV2 #
##############

import os
import wmi
import sys
import time
import uuid
import psutil
import ctypes
import winreg
import fnmatch
import pathlib
import subprocess
import pywinauto

#misc
abnormal = 0
c = wmi.WMI()

# ctypes shtuff
# user32
user32 = ctypes.windll.user32
enumwin = user32.EnumWindows
enumwinproc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
getwintext = user32.GetWindowTextW
getwintextlen = user32.GetWindowTextLengthW
winvis = user32.IsWindowVisible

# kernel32, ntdll
kernel32 = ctypes.windll.kernel32
ntdll = ctypes.WinDLL("ntdll.dll")

# debug check ###############################
def SecondAnti():
    try:
        proc_handle = kernel32.GetCurrentProcess()
        dbg_dtc = ctypes.c_int(0)
        kernel32.CheckRemoteDebuggerPresent(proc_handle, ctypes.byref(dbg_dtc))
        return dbg_dtc.value != 0
    except Exception as e:
        print(f"[SECONDANTI - FAIL]\n{e}")
#############################################

dtc_win = False
def checkwin(hwnd, par):
    global dtc_win
    length = getwintextlen(hwnd)
    if length == 0:
        return False

    buf = ctypes.create_unicode_buffer(length + 1)
    getwintext(hwnd, buf, length + 1)
    title = buf.value
    lower_title = title.lower()

    for p in procTitles:
        if winvis(hwnd) and title and p in lower_title:
            dtc_win = True
            print("[DETECTED VM/DEBUG - BLACKLISTED WINDOW TITLE]")
            print(f"Matched keyword: {p}\nWinTitle: {title}\n")
            return False

    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
    def enum_child(hwnd_child, param):
        clen = getwintextlen(hwnd_child)
        if clen == 0:
            return True
        cbuf = ctypes.create_unicode_buffer(clen + 1)
        getwintext(hwnd_child, cbuf, clen + 1)
        child_title = cbuf.value.lower()
        for p in procTitles:
            if p in child_title:
                global dtc_win
                dtc_win = True
                print("[DETECTED VM/DEBUG - BLACKLISTED CHILD WINDOW TEXT]")
                print(f"Matched keyword: {p}\nChildWinText: {cbuf.value}\n")
                return False
        return True

    if not ctypes.windll.user32.EnumChildWindows(hwnd, enum_child, 0):
        return False

    try:
        from pywinauto import Desktop
        seen_texts = set()
        windows = Desktop(backend="uia").windows()
        for win in windows:
            try:
                wtext = win.window_text().strip().lower()
                if wtext and wtext not in seen_texts:
                    seen_texts.add(wtext)
                    for p in procTitles:
                        if p in wtext:
                            dtc_win = True
                            print("[DETECTED VM/DEBUG - BLACKLISTED WINDOW TITLE]")
                            print(f"Matched keyword: {p}\nWinTitle: {win.window_text()}\n")
                            return False

                for child in win.descendants():
                    try:
                        ctext = child.window_text().strip().lower()
                        if not ctext or ctext in seen_texts:
                            continue
                        seen_texts.add(ctext)
                        for p in procTitles:
                            if p in ctext:
                                dtc_win = True
                                print("[BLACKLISTED NAME DETECTED - BLACKLISTED CHILD ELEMENT]")
                                print(f"Matched keyword: {p}\nChildElem: {child.window_text()}\n")
                                return False
                    except:
                        continue
            except:
                continue
    except:
        pass
    return True

ranges = [
    ("00:50:56", "00:00:00", "FF:FF:FF"), #VMWare
    ("00:0C:29", "00:00:00", "FF:FF:FF"),
    ("00:05:69", "00:00:00", "FF:FF:FF"),
    ("00:1C:14", "00:00:00", "FF:FF:FF"),
    ("00:50:56", "80:00:00", "BF:FF:FF"),
    ("08:00:27", "00:00:00", "FF:FF:FF"), # VBox
    ("00:16:3E", "00:00:00", "FF:FF:FF"), # RedHat XEN
    ("00:1D:D8", "00:00:00", "FF:FF:FF"), # Microsoft SCVMM Hyper-V
    ("00:03:FF", "00:00:00", "FF:FF:FF"), # Microsoft Virtual PC/Server
    ("00:18:51", "00:00:00", "FF:FF:FF"), # SWsoft
    ("58:9C:FC", "00:00:00", "FF:FF:FF"), # bhyve (FreeBSDF)
    ("50:6B:8D", "00:00:00", "FF:FF:FF"), # Nutanix AHV
    ("54:52:00", "00:00:00", "FF:FF:FF"), # KVM
    ("54:52:FF", "00:00:00", "FF:FF:FF"),
    ("52:54:00", "00:00:00", "FF:FF:FF"),
    ("96:00:00", "00:00:00", "FF:FF:FF"), # Hetzner VServer
    ("96:00:FF", "00:00:00", "FF:FF:FF"),
    ("00:1C:42", "00:00:00", "FF:FF:FF"), # Parallels
]

def mac2int(mac):
    mac = mac.replace(":", "").replace("-", "")
    return int(mac, 16)

def check_range(mac, prefix, start, end):
    mac_int = mac2int(mac)
    prefix_int = mac2int(prefix + ":00:00:00")

    start_int = mac2int(prefix + ":" + start)
    end_int = mac2int(prefix + ":" + end)

    return start_int <= mac_int <= end_int

def check_gpu():
    if video.Name == "Microsoft Basic Display Adapter":
        return True
    elif "virtualbox" in video.Name or "vmware" in video.Name:
        return True
    else:
        return False

def termination():  # Set itself as critical process - and terminate the program.
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
    sys.exit(0)


start = "00:00:00"
end = "FF:FF:FF"
raw_mac = uuid.getnode()
address = ':'.join(['{:02x}'.format((raw_mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

# File entires borrowed from PySilon, added many more entries.

files = [
    "C:\\windows\\system32\\vboxhook.dll", # VBox
    "C:\\windows\\system32\\vboxmrxnp.dll", # VBox
    "C:\\windows\\system32\\drivers\\VBoxMouse.sys", # VBox
    "C:\\windows\\system32\\drivers\\VBoxGuest.sys", # VBox
    "C:\\windows\\system32\\drivers\\VBoxSF.sys", # VBox
    "C:\\windows\\system32\\drivers\\VBoxVideo.sys", # VBox
    "C:\\program files\\oracle\\virtualbox guest additions\\*", # VBox
    "C:\\windows\\system32\\vmGuestLib.dll", # VMWare/VBox
    "C:\\windows\\system32\\vm3dgl.dll", # VMWare/VBox
    "C:\\windows\\system32\\vmsrvc.dll", # VMWare/VBox
    "C:\\windows\\system32\\vmsrvc.sys", # VMWare/VBox
    "C:\\windows\\system32\\vmmouse.sys", # VMWare/VBox
    "C:\\program files\\VMware\\*", # VMWare
    "C:\\windows\\system32\\drivers\\KsDumperDriver.sys", # KSDumper11
    "C:\\windows\\system32\\drivers\\balloon.sys", # KVM
    "C:\\windows\\system32\\drivers\\netkvm.sys", # KVM
    "C:\\windows\\system32\\drivers\\vioinput*", # KVM
    "C:\\windows\\system32\\drivers\\viofs.sys", # KVM
    "C:\\windows\\system32\\drivers\\vioser.sys", # KVM
    "C:\\windows\\system32\\drivers\\qemu-ga", # QEMU\KVM
    "C:\\windows\\system32\\drivers\\qemuwmi", # QEMU\KVM
    "C:\\windows\\system32\\drivers\\prl_sf*", # Parallels
    "C:\\windows\\system32\\drivers\\prl_tg*", # Parallels
    "C:\\windows\\system32\\drivers\\prl_eth*", # Parallels
    "C:\\program files (x86)\\httpdebuggerpro\\httpdebuggersvc.exe", # HTTP Debugger Pro Service
    ]

procs = [
    # QEMU \ KVM
    "qemu-ga.exe",
    "vmusrvc.exe",
    "vmusrvc.exe",

    #VMWare
    "vmtoolsd.exe",
    "vmwaretray.exe"
    "vmwareuser.exe",
    "vmwaretray.exe",
    "vgauthservice.exe",
    "vmacthlp.exe",
    "tpautoconnsvc.exe",

    #VirtualBox
    "vboxservice.exe",
    "vboxtray.exe",
    "vboxcontrol.exe",

    # Misc. VM/Sandbox
    "prl_cc.exe"
    "prl_tools.exe",
    "xenservice.exe",
    "qemu-ga.exe",
    "joeboxcontrol.exe",
    "joeboxserver.exe",
    
    # Network Debuggers
    "fakenet.exe",
    "dumpcap.exe",
    "httpdebuggerui.exe",
    "httpdebuggerpro.exe",
    "wireshark.exe",
    "fiddler.exe",
    "fiddler everywhere.exe",
    "progress telerik fiddler web debugger.exe",
    "dumpcap.exe",
    "charles.exe",
    "burpsuitepro.exe",
    "burpsuite.exe",
    "burpsuitecommunity.exe",
    "mitmweb.exe",
    "mitmproxy.exe",
    "mitmdump.exe",
    "insomnia.exe",
    "http toolkit.exe",
    "postman.exe",
    "reqable.exe",
    "echo mirage.exe",

    # Debuggers/Disassemblers
    "x32dbg.exe",
    "x64dbg.exe",
    "x96dbg.exe",
    "idag.exe",
    "idag64.exe",
    "idaw.exe",
    "idaw64.exe",
    "ida32.exe",
    "ida64.exe",
    "idaq.exe",
    "windbg.exe",
    "immunitydebugger.exe",
    "windasm.exe",
    "ollydbg.exe",
    "pestudio.exe",
    "binaryninja.exe",
    "cheat engine.exe",
    "cheatengine-i386.exe",
    "cheatengine-x86_64.exe",
    "cheatengine-x86_64-sse4-avx2.exe",
    "nopde engine.exe",
    "nopdeengine-i386.exe",
    "nopdeengine-x86_64.exe",
    "nopdeengine-x86_64-sse4-avx2.exe",
    "dnspy.exe",
    "DbgX.Shell.exe",
    "ILSpy.exe",
    "gdb.exe",

    # Dumpers
    "ksdumperclient.exe",
    "ksdumper.exe",
    "ksdumper11.exe",
    "kdu.exe", # KsDumper driver loader
    
    # Misc.
    "df5serv.exe",
    "regedit.exe",

    # Process Monitors
    "sysmon.exe",
    "sysmon64.exe",
    "procmon.exe",
    "procmon64.exe",
    "procexp.exe",
    "procexp64.exe",
    "systeminformer.exe",
    "processhacker.exe",
]

procTitles = [
    "proxifier", "graywolf", "extremedumper", "exeinfope", "dnspy",
    "titanHide", "ilspy", "titanhide", "x32dbg", "codecracker", "simpleassembly",
    "process hacker 2", "pc-ret", "http debugger", "Centos", "process monitor",
    "debug", "ILSpy", "reverse", "simpleassemblyexplorer", "de4dotmodded",
    "dojandqwklndoqwd-x86", "sharpod", "folderchangesview", "fiddler", "die",
    "crack", "strongod", "ida -", "brute", "dump", "StringDecryptor", "wireshark",
    "debugger", "httpdebugger", "gdb", "kdb", "x64_dbg", "windbg", "x64netdumper",
    "petools", "scyllahide", "megadumper", "reversal", "ksdumper v1.1 - by equifox",
    "dbgclr", "ollydbg", "ksdumper", "wpe pro", "httpanalyzer", "httpdebug", "PhantOm", 
    "kgdb", "james", "x32_dbg", "proxy", "phantom", "mdbg", "WPE PRO", "system explorer",
    "de4dot", "X64NetDumper", "protection_id", "charles", "systemexplorer", "procmon64",
    "MegaDumper", "ghidra", "0harmony", "dojandqwklndoqwd", "hacker", "process hacker",
    "harmony", "Protection_ID", "PETools", "scyllaHide", "x96dbg", "systemexplorerservice",
    "mitmproxy", "sniffer", "Process Hacker", "Process Explorer",
    "Sysinternals", "www.sysinternals.com", "binary ninja", "titanengine"
]

usernames = [
    "johnson",
    "miller",
    "malware",
    "maltest",
    "currentuser",
    "sandbox",
    "virus",
    "john doe",
    "test user",
    "sand box",
    "wdagutilityaccount"
]

drivers = os.listdir("C:\\windows\\system32\\drivers\\")
procmon = "PROCMON*.sys"
procexp = "PROCEXP*.sys"

system_creation_time = psutil.Process(4)
humanized = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(system_creation_time.create_time()))
video = c.Win32_VideoController()[0]
mon_width = user32.GetSystemMetrics(0)
mon_height = user32.GetSystemMetrics(1)

current_user = os.getenv("USERNAME", "").lower()

for file in drivers: # Try find the loaded ProcMon / ProcExp
    if fnmatch.fnmatch(file, procmon) or fnmatch.fnmatch(file, procexp):
        print("[DETECTED LOADED PROCMON/PROCEXP DRIVERS]")
        print(f"{file}\n")

# Time to defeat any.run/most online VMs :^)
if humanized == "1970-01-01 00:00:00": # Check the System startup time, any.run reports as 1970-01-01
    print("[ABNORMAL ENVIRONMENT - SYSTEM STARTUP TIME]\n")
    abnormal + 1

if video.Name == "PNVURV": # Check for PNY graphics card (server-grade)
    print("[ABNORMAL ENVIRONMENT - SERVER-GRADE (PNY) GRAPHICS")
    abnormal + 1

if check_gpu(): # Check if there is a GPU installed at all
    print("[DETECTED POSSIBLE VM - NO GPU INSTALLED]\n")

if video.InstalledDisplayDrivers == None: # Check if system has any GPU drivers installed
    print("[DETECTED POSSIBLE VM - NO GRAPHICS DRIVERS INSTALLED]\n")

if abnormal >= 2: # Check abnormality score
    print("[ABNORMALITY SCORE ABOVE 2 - PROBABLE VM]")

for process in psutil.process_iter(['pid', 'name']): # Iterates through all the processes and checks if it matches one of the blacklisted processes
    if process.info['name'].lower() in procs:
        print("[DETECTED VM/DEBUG - BLACKLISTED PROCESS]")
        print(f"{process.info['name']}\n")

for file_path in files: # Iterates through all the paths and checks if its a valid file
    if os.path.exists(file_path):
        print("[DETECTED VM/DEBUG - BLACKLISTED DRIVER/FILE]")
        print(f"{file_path}\n")

if kernel32.IsDebuggerPresent() != 0: # Check the IsDebuggerPresent value (kernel32.dll)
    print("[DETECTED DEBUG - ISDEBUGGERPRESENT > 0]")
    print("kernel32.IsDebuggerPresent: " + kernel32.IsDebuggerPresent())

if SecondAnti(): # Check the value of CheckRemoteDebuggerPresent (kernel32.dll)
    print("[DETECTED DEBUG - REMOTE DEBUGGER]")
    print("kernel32.CheckRemoteDebuggerPresent: " + SecondAnti())

temp = subprocess.check_output(['wmic', 'diskdrive', 'get', 'model'], text=True)
if "DADY HARDDISK" in temp or "QEMU HARDDISK" in temp: # Check if the drive matches either, belongs to VMs
    print("[DETECTED VM - DADY/QEMU DRIVE]")
    print("Drive Model: " + temp)

for prefix, start, end in ranges: # Check if user MAC address belongs to VM provider range
    if check_range(address, prefix, start, end):
        print("[MAC ADDRESS BELONGS TO VM RANGE]")
        print(f"USER: {address}\nRANGE: {prefix}:{start} - {prefix}:{end}\n")

if current_user in usernames: # Check if the current computer username belongs to a widely known sandbox user
    print("[DETECTED POSSIBLE VM - BLACKLISTED USERNAME]")
    print("Detected user: " + current_user)

if mon_width < 800 or mon_height < 600: # Check if the current monitor resolution is smaller than 800x600 (or smaller), no one will be running this res unless it's a VM.
    print("[DETECTED SUSPICIOUS ENVIRONMENT - RES < 800X600]")
    print(f"Monitor Width: {mon_width}\nMonitor Height: {mon_height}")

for sys in c.Win32_ComputerSystem(): # Check if one of the strings are prsent inside the system manufacturer/model, indicating a VM
    manu = sys.Manufacturer.lower()
    model = sys.Model.lower()
    hyperv = getattr(sys, "HypervisorPresent", False)
    if "microsoft corporation" in manu and "virtual" in model or "vmware" in manu or "vmware" in model or "virtualbox" in model:
        print("[DETECTED VM - MANU/MODEL]")
        print(f"Manufacturer: {manu}\nModel: {model}\n")

wincheck = enumwin(enumwinproc(checkwin), 0) # Run the process window title check - made seperate for iteration purposes

try: # Lets try detect VMWare/VBox BIOS
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
    smanu, _ = winreg.QueryValueEx(key, "SystemManufacturer")
    sbiosver, _    = winreg.QueryValueEx(key, "SystemBiosVersion")
    if smanu and ("vmware" in smanu.lower() or "virtualbox" in smanu.lower()):
        print("[DETECTED VM - BIOS CHECK]")
        print("System Manufacturer BIOS: " + smanu)
except FileNotFoundError:
    print("[BIOS CHECK - FAIL TO FIND KEY OR VALUE]")
except Exception as e:
    print("\nFailed to run BIOS check\n", e)

tmp = input("\n\nPress ENTER to exit...")
exit()
