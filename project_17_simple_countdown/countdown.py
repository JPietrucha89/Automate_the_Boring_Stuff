# Let’s write a countdown program that plays an alarm at the end of the countdown.

# At a high level, here’s what your program will do:
# Count down from 60.
# Play a sound file(alarm.wav) when the countdown reaches zero.

# This means your code will need to do the following:
# Pause for 1 second in between displaying each number in the countdown by calling time.sleep().
# Call subprocess.Popen() to open the sound file with the default application.

import time
import os
from pathlib import Path
import subprocess

seconds_countdown = 10

for i in range(seconds_countdown, 0, -1):
    print(i)
    time.sleep(1)

subprocess.Popen(['start', Path(
    os.getcwd(), 'project_17_simple_countdown', 'alarm.wav')], shell=True)
#subprocess.Popen(Path(os.getcwd(), 'project_17_simple_countdown', 'alarm.wav'))
