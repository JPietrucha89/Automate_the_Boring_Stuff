import time
import datetime

startTime = time.time()
dt = datetime.datetime.now()
print('Printing datetime object and it\'s components...')
print(dt)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

# Comparing dates, finding which one is greater/bigger/newer
print('Comparing dates...')
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(newyears2020 > halloween2019)
print(newyears2020 != oct31_2019)

# TIMEDELTA ------------------------------------------------------------------------------
# The datetime module also provides a timedelta data type, which represents a duration of time rather than a moment in time.
# To create a timedelta object, use the datetime.timedelta() function. The datetime.timedelta() function takes keyword arguments:
# weeks, days, hours, minutes, seconds, milliseconds, and microseconds
# There is no month or year keyword argument, because “a month” or “a year” is a variable amount of time depending on the particular month or year. A timedelta object has the total duration represented in days, seconds, and microseconds. These numbers are stored in the days, seconds, and microseconds attributes, respectively. The total_seconds() method will return the duration in number of seconds alone. Passing a timedelta object to str() will return a nicely formatted, human-readable string representation of the object.
print('Printing timedelta object and it\'s componets')
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# This timedelta object’s <days> attributes stores 11, and its <seconds> attribute stores 36548 (10 hours, 9 minutes, and 8 seconds, expressed in seconds). Calling total_seconds() tells us that 11 days, 10 hours, 9 minutes, and 8 seconds is 986,948 seconds.
print(delta.days, delta.seconds, delta.microseconds)  # (11, 36548, 0)
print(delta.total_seconds())  # 986948.0
print(str(delta))  # '11 days, 10:09:08'

# The arithmetic operators can be used to perform date arithmetic on datetime values. For example, to calculate the date 1, 000 days from now:
thousandDays = datetime.timedelta(days=1000)
dt = datetime.datetime.now()
print('Thousand days from now: ', dt+thousandDays)

# timedelta objects can be added or subtracted with datetime objects or other timedelta objects using the + and - operators. A timedelta object can be multiplied or divided by integer or float values with the * and / operators.
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print('21.10.2019: ', oct21st)
print('~30 years earlier:', oct21st - aboutThirtyYears)
print('~60 years earlier:', oct21st - (2 * aboutThirtyYears))

# Converting datetime Objects into Strings-----------------------------------------------------------------------------
# Epoch timestamps and datetime objects aren’t very friendly to the human eye. Use the strftime() method to display a datetime object as a string. (The f in the name of the strftime() function stands for format.) The strftime() method uses directives similar to Python’s string formatting.
# strftime() directive    Meaning
#     %Y                  Year with century, as in '2014'
#     %y                  Year without century, '00' to '99' (1970 to 2069)
#     %m                  Month as a decimal number, '01' to '12'
#     %B                  Full month name, as in 'November'
#     %b                  Abbreviated month name, as in 'Nov'
#     %d                  Day of the month, '01' to '31'
#     %j                  Day of the year, '001' to '366'
#     %w                  Day of the week, '0' (Sunday) to '6' (Saturday)
#     %A                  Full weekday name, as in 'Monday'
#     %a                  Abbreviated weekday name, as in 'Mon'
#     %H                  Hour(24-hour clock), '00' to '23'
#     %I                  Hour(12-hour clock), '01' to '12'
#     %M                  Minute, '00' to '59'
#     %S                  Second, '00' to '59'
#     %p                  'AM' or 'PM'
#    '%%                  Literal '%' character
may2nd = datetime.datetime(2022, 5, 2, 21, 37, 0)
print(may2nd.strftime('%Y/%m/%d %H:%M:%S'))
print(may2nd.strftime('%I:%M %p'))
print(may2nd.strftime("%B of '%y"))

# Converting datetime Objects into Strings-----------------------------------------------------------------------------
# If you have a string of date information, such as '2019/10/21 16:29:00' or 'October 21, 2019', and need to convert it to a datetime object, use the datetime.datetime.strptime() function. The strptime() function is the inverse of the strftime() method. A custom format string using the same directives as strftime() must be passed so that strptime() knows how to parse and understand the string. (The p in the name of the strptime() function stands for parse.)
print(datetime.datetime.strptime('May 2, 2022', '%B %d, %Y'))
print(datetime.datetime.strptime('2022/05/02 21:37:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("May of '22", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))


totalTime = time.time() - startTime
print('Time passed: ', round(totalTime, 2))

# Review of Python’s Time Functions
# Dates and times in Python can involve quite a few different data types and functions. Here’s a review of the three different types of values used to represent time:

# A Unix epoch timestamp(used by the time module) is a float or integer value of the number of seconds since 12 AM on January 1, 1970, UTC.
# A datetime object(of the datetime module) has integers stored in the attributes year, month, day, hour, minute, and second.
# A timedelta object(of the datetime module) represents a time duration, rather than a specific moment.
# Here’s a review of time functions and their parameters and return values:

# time.time() This function returns an epoch timestamp float value of the current moment.

# time.sleep(seconds) This function stops the program for the number of seconds specified by the seconds argument.

# datetime.datetime(year, month, day, hour, minute, second) This function returns a datetime object of the moment specified by the arguments. If hour, minute, or second arguments are not provided, they default to 0.

# datetime.datetime.now() This function returns a datetime object of the current moment.

# datetime.datetime.fromtimestamp(epoch) This function returns a datetime object of the moment represented by the epoch timestamp argument.

# datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds) This function returns a timedelta object representing a duration of time. The function’s keyword arguments are all optional and do not include month or year.

# total_seconds() This method for timedelta objects returns the number of seconds the timedelta object represents.

# strftime(format) This method returns a string of the time represented by the datetime object in a custom format that’s based on the format string.

# datetime.datetime.strptime(time_string, format) This function returns a datetime object of the moment specified by time_string, parsed using the format string argument. See Table 17-1 for the format details.
