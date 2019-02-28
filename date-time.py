# Zoe Cahill - Question 8 Solution
# Changed the name to date-time.py instead of datetime.py as specified in problem sheet
# as python was importing this file rather that the datetime functions I needed

# Imports date time function as we will be need this in out program
import datetime

# Defines a function which will decide what suffix is needed for the date (ie 1st, 2nd, 3rd, 4th all have different suffixes) 
# It will take the variable day. Adapted from https://www.robjwells.com/2013/10/date-suffixes-in-python/
def daysuffix(day):
    # Defines all the days which will take the th suffix
    if 3 < day < 21 or 23 < day < 31:
        # If day matches any of these conditions then function will return th
        return 'th'
    # Otherwise it has to be one of the other 3
    else:
        # Defines the conditions to return the different suffixes
        # %10 reduces the testing to just 1 number for simplicity
        return {1: 'st', 2: 'nd', 3: 'rd'}[day % 10]

# This function will find the current date and time and format as per the problem sheet
def currentdatetime():
    # This line will get the current time and date and assign it to the variable current
    current = datetime.datetime.now()
    # This line will print and format the date.
    # Inside the format statement we will call the daysuffix function to decide the suffix of the day
    print(current.strftime("%A, %B %d{suffix} %Y at %I:%M%p").format(suffix=daysuffix(current.day)))

currentdatetime()
