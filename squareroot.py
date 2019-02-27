# Zoe Cahill -  Question 7 Solution

def sqrt():
    # Imports a function from PCInput.py created to handle user input
    from PCInput import getFloat
    from math import sqrt

    # Describes program to user
    print ("This program will tell you the approximate square root of a positive number")
    
    # Calls function imported above
    # This will check that the user has inputted a positive value only and will return a float value
    num = getFloat("Please input a number: ")

    print ("The answer is {:.1f}".format(sqrt(num)))

sqrt()



