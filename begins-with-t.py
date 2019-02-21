# Zoe Cahill - Question 2 Solution

# Need to import this as we will be using some functions within datetime for our program
import datetime

# Describes the program to the user
print ("This program will check if today begins with a \"T\" or not")

# Checks what todays date is and assigns it to variable x
day = datetime.datetime.now() 
# Formats that date to the weekday full version
day = day.strftime("%A") 

# Checks if the first letter of the string is T or not
if day[0] == "T": 
    print ("Today is" , day , "so it does begin with a \"T\"!")
else: 
    print ("Today is", day , "so it does not begin with a \"T\"!")
