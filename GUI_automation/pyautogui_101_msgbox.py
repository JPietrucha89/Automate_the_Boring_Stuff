import pyautogui

# Displaying Message Boxes-----------------------
# The programs you’ve been writing so far all tend to use plaintext output (with the print() function) and input (with the input() function). However, PyAutoGUI programs will use your entire desktop as its playground. The text-based window that your program runs in, whether it’s Mu or a Terminal window, will probably be lost as your PyAutoGUI program clicks and interacts with other windows. This can make getting input and output from the user hard if the Mu or Terminal windows get hidden under other windows.

# Here are four message box functions:

# Displays text and has a single OK button.
pyautogui.alert('This is a message.', 'Important')

# Displays text and has OK and Cancel buttons, returning either 'OK' or 'Cancel' depending on the button clicked.
pyautogui.confirm('Do you want to continue?')

# Displays text and has a text field for the user to type in , which it returns as a string.
pyautogui.prompt("What is your cat's name?")

# Is the same as prompt(), but displays asterisks so the user can enter sensitive information such as a password.
pyautogui.password('What is the password?')
