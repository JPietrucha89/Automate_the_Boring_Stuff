# When Python logs an event, it creates a LogRecord object that holds information about that event. The logging module’s basicConfig() function lets you specify what details about the LogRecord object you want to see and how you want those details displayed.
# Logging levels provide a way to categorize your log messages by importance. There are five logging levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# Passing logging.DEBUG to the basicConfig() function’s level keyword argument will show messages from all the logging levels (DEBUG being the lowest level). But after developing your program some more, you may be interested only in errors. In that case, you can set basicConfig()’s level argument to logging.ERROR. This will show only ERROR and CRITICAL messages and skip the DEBUG, INFO, and WARNING messages.

# The logging.disable() function disables these so that you don’t have to go into your program and remove all the logging calls by hand. You simply pass logging.disable() a logging level, and it will suppress all log messages at that level or lower. So if you want to disable logging entirely, just add logging.disable(logging.CRITICAL)

# Instead of displaying the log messages to the screen, you can write them to a text file. The logging.basicConfig() function takes a filename keyword argument, like so:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG) # disables all debugs of level DEBUG and lower

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')