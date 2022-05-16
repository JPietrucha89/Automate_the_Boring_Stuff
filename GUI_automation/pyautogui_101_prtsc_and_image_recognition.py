import pyautogui
import os
from pathlib import Path

# Using CMD tool MouseInfo makes this part a lot easier
# import pyautogui
# pyautogui.mouseInfo()

# Analyzing the screenshot -----------------------------------
pix = pyautogui.pixel(0, 0)  # returns RGB value of given pixel
print(pix)

# PyAutoGUI’s pixelMatchesColor() function will return True if the pixel at the given x- and y-coordinates on the screen matches the given color. The first and second arguments are integers for the x- and y-coordinates, and the third argument is a tuple of three integers for the RGB color the screen pixel must match.
print(pyautogui.pixelMatchesColor(0, 0, (46, 52, 64)))
print(pyautogui.pixelMatchesColor(1603, 665, (46, 52, 64)))

# Finding image/icon within screenshot -----------------------------
# create PIL.Image.Image object
prtsc = pyautogui.screenshot(
    Path(os.getcwd(), 'GUI_automation', 'screentshot.png'))

# get location of Slack icon on prinstcreen
# returns of tuple with coordinates
position = pyautogui.locateCenterOnScreen(
    (str(Path(os.getcwd(), 'GUI_automation', 'Slack_icon.png'))))

if position is not None:
    x_axis, y_axis = position[0], position[1]

    # move mouse to found position and do a mouse click
    pyautogui.moveTo(x_axis, y_axis, duration=1)
    pyautogui.click()

# Obtaining the Active Window --------------------------------------
# The active window on your screen is the window currently in the foreground and accepting keyboard input.
window_obj = pyautogui.getActiveWindow()
print('Printing: left, right, top, bottom')
print(window_obj.left)
print(window_obj.right)
print(window_obj.top)
print(window_obj.bottom)

print('Printing: topleft, topright, bottomleft, bottomright')
print(window_obj.topleft)
print(window_obj.topright)
print(window_obj.bottomleft)
print(window_obj.bottomright)

print('Printing: midleft, midright, midtop, midbottom')
print(window_obj.midleft)
print(window_obj.midright)
print(window_obj.midtop)
print(window_obj.midbottom)

print('Printing: size')
print(window_obj.size)
print('Printing: area')
print(window_obj.area)

print('Printing: width, height')
print(window_obj.width)
print(window_obj.height)

print('Printing: center')
print(window_obj.center)

print('Printing: title')
print(window_obj.title)

# Other Ways of Obtaining Windows ---------------------------------
# While getActiveWindow() is useful for obtaining the window that is active at the time of the function call, you’ll need to use some other function to obtain Window objects for the other windows on the screen.

# The following functions return a list of objects. If they’re unable to find any windows, they return an empty list:

# Returns a list of Window objects for every visible window on the screen.
print(pyautogui.getAllWindows())

# pyautogui.getWindowsAt(x, y) Returns a list of Window objects for every visible window that includes the point(x, y).
print(pyautogui.getWindowsAt(100, 100))

# returns a list of Window objects for every visible window that includes the string title in its title bar.
print(pyautogui.getWindowsWithTitle('py'))

# returns a list of strings of every visible window.
print(pyautogui.getAllTitles())

# Manipulating Windows ------------------------------------------
# Windows attributes can do more than just tell you the size and position of the window. You can also set their values in order to resize or move the window.
window_obj = pyautogui.getActiveWindow()
print(window_obj.width)
print(window_obj.topleft)

# move window
window_obj.width = 1000
window_obj.topleft = (800, 400)

print(window_obj.isActive)
print(window_obj.isMaximized)
print(window_obj.isMinimized)

window_obj.minimize()
window_obj.maximize()
