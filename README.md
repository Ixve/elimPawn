# elimPawn
elimPawn is a batch-based dropper for sneaky malware, which utilizes the Visual Studio "pre-build setup" in order to run malicious batch code.

# File Structure
* / - Contains all of the pyarmor'd files/EXEs, including the main stealer.
* /DEV/ - Contains all of the files, pre-encoded/pre-obfuscated & encoded/obfuscated.

# Stages
* [Stage 0 - IP Check]<br>Checks the IP by comparing the IPs ASN to a list of known bad ASNs, this isn't the best check, but it works for the most part:tm: - if it gets a hit, exits all `conhost.exe`, `cmd.exe` and `powershell.exe` processes.<br><br>
* [Stage 1 - Elevation]<br>Elevates the current shell by making and running a VBS script.<br><br>
* [Stage 2 - WinDefender Exclusion]<br>Excludes the `C:\Users\Public` path from Windows Defender using good ole' PowerShell.<br><br>
* [Stage 3 - Environment Check]<br>Downloads and runs a Python script pre-packaged with PyInstaller and obfuscated using PyArmor, the script checks if it's being ran in a sandbox environment and if there is network debugging, anyone with a brain would be able to bypass this so this should be aimed at dumb people downloading everything off the internet.<br><br>
* [Stage 4 - Payload Drop]<br>We have now detached from our shitty batch and will run everything from the Python script. The script will drop a secondary payload after all the checks have passed.<br><br>
* [Stage 5 - Execution]<br>After dropping our payload we will run it as we're already elevated from our command prompt environment.<br><br>

# Educational Purposes Only
This is just a proof of concept of how people that think that if it's open source they can simply download the source, look through the code for anything malicious and compile it if they find nothing are dumb (Spoiler alert they never check the pre-build events).
