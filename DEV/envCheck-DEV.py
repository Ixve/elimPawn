############
# elimPawn #
#################################################################################
#                                                                                #
# envCheck-DEV.py                                                                #
# You can look through this file if you're interested in what the script does :) #
#                                                                                #
##################################################################################

import os
import wmi
import time
import uuid
import psutil
import fnmatch

abnormal = 0
c = wmi.WMI()

ranges = [
    ("00:50:56", "00:00:00", "FF:FF:FF"), #VMWare
    ("00:0C:29", "00:00:00", "FF:FF:FF"),
    ("00:05:69", "00:00:00", "FF:FF:FF"),
    ("00:1C:14", "00:00:00", "FF:FF:FF"),
    ("00:50:56", "80:00:00", "BF:FF:FF"),
    ("00:16:3E", "00:00:00", "FF:FF:FF"), # RedHat XEN
    ("00:1D:D8", "00:00:00", "FF:FF:FF"), # Microsoft SCVMM Hyper-V
    ("00:03:FF", "00:00:00", "FF:FF:FF"), # Microsoft Virtual PC/Server
    ("00:18:51", "00:00:00", "FF:FF:FF"), # SWsoft
    ("58:9C:FC", "00:00:00", "FF:FF:FF"), # bhyve (FreeBSDF)
    ("50:6B:8D", "00:00:00", "FF:FF:FF"), # Nutanix AHV
    ("54:52:00", "00:00:00", "FF:FF:FF"), # KVM
    ("54:52:FF", "00:00:00", "FF:FF:FF"),
    ("96:00:00", "00:00:00", "FF:FF:FF"), # Hetzner VServer
    ("96:00:FF", "00:00:00", "FF:FF:FF")
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

start = "00:00:00"
end = "FF:FF:FF"
raw_mac = uuid.getnode()
address = ':'.join(['{:02x}'.format((raw_mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

# Entires borrowed from PySilon, added many more entries.

files = [
    "C:\\windows\\system32\\vmGuestLib.dll",
    "C:\\windows\\system32\\vm3dgl.dll",
    "C:\\windows\\system32\\vboxhook.dll",
    "C:\\windows\\system32\\vboxmrxnp.dll",
    "C:\\windows\\system32\\vmsrvc.dll",
    "C:\\windows\\system32\\drivers\\vmsrvc.sys",
    "C:\\windows\\system32\\drivers\\KsDumperDriver.sys",
    "C:\\program files (x86)\httpdebuggerpro\httpdebuggersvc.exe",
    ]

procs = [
    #VMWare
    "vmtoolsd.exe",
    "vmwaretray.exe"
    "vmwareuser.exe",
    "vmwaretray.exe",
    "vgauthservice.exe",
    "vmacthlp.exe",

    #VirtualBox
    "vboxservice.exe",
    "vboxtray.exe",

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
    "ida32.exe",
    "ida64.exe",
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

    # Dumpers
    "ksdumperclient.exe",
    "ksdumper.exe",
    "ksdumper11.exe",
    "kdu.exe", # KsDumper driver loader
    
    # Misc.
    "df5serv.exe",

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

drivers = os.listdir("C:\\windows\\system32\\drivers\\")
procmon = "PROCMON*.sys"
procexp = "PROCEXP*.sys"

system_creation_time = psutil.Process(4)
humanized = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(system_creation_time.create_time()))
video = c.Win32_VideoController()[0]

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

if video.Name == "Microsoft Basic Display Adapter": # Check if there is a GPU installed at all
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

for prefix, start, end in ranges: # Check if user MAC address belongs to VM provider range
    if check_range(address, prefix, start, end):
        print("[MAC ADDRESS BELONGS TO VM RANGE]")
        print(f"USER: {address}\nRANGE: {prefix}:{start} - {prefix}:{end}\n")


tmp = input("Press any key to exit...")
exit()
