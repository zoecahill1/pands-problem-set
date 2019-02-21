# Zoe Cahill - Question 4 Solution

# Imports a function from PCInput which was created to handle user input
from PCInput import getPosInt 

# Calls the fuction imported above
# This function will check that the number entered is a positive integer only
num = getPosInt("Please enter a poisitve number: ")

# Check will run until number gets to 1
while num!=1:
    # Prints the current value of num. Have to cast int type as anything divided becomes a float type.
    print(int((num)))
    # Checking to see if number is even (there will be no remainder if it is)
    if num%2 == 0:
        # If this check returns true then program will divide num by 2
        num=num/2
    # Otehrwise then number is not even so it must be odd
    else:
        # When number is odd we multiply by 3 and add 1
        num = (num*3)+1
    # Returns control to beginning of loop to check next number
    continue
# Prints out last number which will be 1
print (int((num)))


