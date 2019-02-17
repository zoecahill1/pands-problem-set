# Question 2

import datetime

print ("This program will check if today begins with a \"T\" or not")
day = datetime.datetime.now() # Checks what todays date is and assigns it to variable x
day = day.strftime("%A") # Formats that date to the weekday full version
if day[0] == "T": # Checks if the first letter of the string is T or not
    print ("Today is" , day , "so it does begin with a \"T\"!")
else: 
    print ("Today is", day , "so it does not begin with a \"T\"!")
