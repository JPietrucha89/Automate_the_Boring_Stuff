import pyautogui

resolution = pyautogui.size()

print(resolution)
print(resolution.width)

print(pyautogui.position())  # returns current position of mouse cursor

# moving mouse cursor to absolute position
pyautogui.moveTo(10, 10)
pyautogui.moveTo(1000, 1000, duration=1.5)

# moving mouse cursor to relative position
pyautogui.moveRel(1000, 0)
pyautogui.moveRel(-1000, 0, duration=1.5)
# there is a drag() method which works the same but holds down LMB - can be used for drawing in Paint ;)

# mouse click. There are also methods fir middleCLick, doubleClick and so on
pyautogui.click(18, 1056)  # click on Start button

# markowanie roboty :D
# safety net - move cursor to topleft corner (position 0,0) to trigger FailSafeException
while True:
    pyautogui.moveRel(100, 0, duration=1)
    pyautogui.moveRel(-100, 0, duration=1)
