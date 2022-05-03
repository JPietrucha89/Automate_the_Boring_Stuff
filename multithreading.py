import threading
import time
print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


# To create a Thread object, we call threading.Thread() and pass it the keyword argument target = takeANap. This means the function we want to call in the new thread is takeANap(). Notice that the keyword argument is target = takeANap, not target = takeANap(). This is because you want to pass the takeANap() function itself as the argument, not call takeANap() and pass its return value.
threadObj = threading.Thread(target=takeANap)
# After we store the Thread object created by threading.Thread() in threadObj, we call threadObj.start() to create the new thread and start executing the target function in the new thread.
threadObj.start()

print('End of program.')

# When this program is run, the output will look like this:
# Start of program.
# End of program.
# Wake up!

# This can be a bit confusing. If print('End of program.') is the last line of the program, you might think that it should be the last thing printed. The reason Wake up! comes after it is that when threadObj.start() is called, the target function for threadObj is run in a new thread of execution. Think of it as a second finger appearing at the start of the takeANap() function. The main thread continues to print('End of program.'). Meanwhile, the new thread that has been executing the time.sleep(5) call, pauses for 5 seconds. After it wakes from its 5-second nap, it prints 'Wake up!' and then returns from the takeANap() function. Chronologically, 'Wake up!' is the last thing printed by the program.
# Normally a program terminates when the last line of code in the file has run ( or the sys.exit() function is called). But threadDemo.py has two threads. The first is the original thread that began at the start of the program and ends after print('End of program.'). The second thread is created when threadObj.start() is called, begins at the start of the takeANap() function, and ends after takeANap() returns.
# A Python program will not terminate until all its threads have terminated. When you ran threadDemo.py, even though the original thread had terminated, the second thread was still executing the time.sleep(5) call.


# Passing Arguments to the Thread’s Target Function --------------------------------------------------------------------------------
# If the target function you want to run in the new thread takes arguments, you can pass the target function’s arguments to threading.Thread(). For example, say you wanted to run this print() call in its own thread:
print('Cats', 'Dogs', 'Frogs', sep=' & ')  # Cats & Dogs & Frogs
# This print() call has three regular arguments, 'Cats', 'Dogs', and 'Frogs', and one keyword argument, sep=' & '. The regular arguments can be passed as a list to the args keyword argument in threading.Thread(). The keyword argument can be specified as a dictionary to the kwargs keyword argument in threading.Thread().

threadObj = threading.Thread(
    target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()  # Cats & Dogs & Frogs
# To make sure the arguments 'Cats', 'Dogs', and 'Frogs' get passed to print() in the new thread, we pass args = ['Cats', 'Dogs', 'Frogs'] to threading.Thread(). To make sure the keyword argument sep = ' & ' gets passed to print() in the new thread, we pass kwargs = {'sep': '& '} to threading.Thread().
# The threadObj.start() call will create a new thread to call the print() function, and it will pass 'Cats', 'Dogs', and 'Frogs' as arguments and ' & ' for the sep keyword argument.

# This is an incorrect way to create the new thread that calls print():
# threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
# What this ends up doing is calling the print() function and passing its return value(print()’s return value is always None) as the target keyword argument. It doesn’t pass the print() function itself. When passing arguments to a function in a new thread, use the threading.Thread() function’s args and kwargs keyword arguments.

# Concurrency Issues -----------------------------------------------------------------------------------------------------------------
# You can easily create several new threads and have them all running at the same time. But multiple threads can also cause problems called concurrency issues. These issues happen when threads read and write variables at the same time, causing the threads to trip over each other. Concurrency issues can be hard to reproduce consistently, making them hard to debug.

# Multithreaded programming is its own wide subject and beyond the scope of this book. What you have to keep in mind is this: to avoid concurrency issues, never let multiple threads read or write the same variables. When you create a new Thread object, make sure its target function uses only local variables in that function. This will avoid hard-to-debug concurrency issues in your programs.
