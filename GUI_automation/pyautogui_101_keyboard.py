import pyautogui

# typewrite is used to type keystrokes
pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!', interval=0.1)

pyautogui.click(100, 100)
pyautogui.typewrite(['A', 'b', 'c', 'left', 'left', 'X', 'Y'], interval=0.1)

# list of all possible keys
print(pyautogui.KEYBOARD_KEYS)

# press single key
pyautogui.press('enter')

# press more than one key - great for keyboard shortcuts
pyautogui.hotkey('ctrl', 'o')
