<img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg">

# lifxstatus_win
Updates LIFX bulbs over local WiFi to reflect your Skype Status (Windows)


Strong dependency on PyAutoGUI. You may find these links useful:

https://pypi.python.org/pypi/PyAutoGUI

https://github.com/asweigart/pyautogui

- You may need to make your own icons (busy.png, available.png etc) because your taskbar background might be a different colour.
- Ensure that your Skype app icon is ALWAYS displayed on your taskbar and not tucked away/hidden. The script relies on the icon being visible on the screen.
- This will not work remotely over RDP for instance. In this case, the `locateOnScreen` function will fail so I just ignore the error and re-try again later.
