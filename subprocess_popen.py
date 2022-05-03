import subprocess

subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# The return value is a Popen object, which has two useful methods: poll() and wait().

# You can think of the poll() method as asking your driver “Are we there yet?” over and over until you arrive. The poll() method will return None if the process is still running at the time poll() is called. If the program has terminated, it will return the process’s integer exit code. An exit code is used to indicate whether the process terminated without errors(an exit code of 0) or whether an error caused the process to terminate(a nonzero exit code—generally 1, but it may vary depending on the program).

# The wait() method is like waiting until the driver has arrived at your destination. The wait() method will block until the launched process has terminated. This is helpful if you want your program to pause until the user finishes with the other program. The return value of wait() is the process’s integer exit code.

# On Windows, enter the following into the interactive shell. Note that the wait() call will block until you quit the launched MS Paint program.
# Here we open an MS Paint process. While it’s still running, we check whether poll() returns None. It should, as the process is still running. Then we close the MS Paint program and call wait() on the terminated process. Now wait() and poll() return 0, indicating that the process terminated without errors.
paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
# True. If .poll() returns None it means that program is still running
print(paintProc.poll() == None)
print(paintProc.wait())  # 0. Doesn't return until MS Paint closes.
print(paintProc.poll())  # 0 means that program was terminated without any errors
