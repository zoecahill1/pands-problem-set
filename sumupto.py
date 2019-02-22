# Zoe Cahill -  Question 1 Solution

# Imports a function from PCInput which was created to handle user input
from PCInput import getPosInt 

# Describes the program to the user
print("This program will output the sum of all the numbers between 1 and whatever you enter into the next line!")

# Calls the function imported above
# This function will check that the number entered is a positive integer only
num = getPosInt("Please enter a positive number: ")

# Initializes the count at 0
ans = 0 

# Uses for loop and range function to loop from 1 to user inputted value
for i in range(1, num+1):
    # Increases count by 1 
    ans = ans + i

# Print out the sum of all the numbers
print (ans)