# Question 1
from PCInput import getPosInt # Imports a function to handle errors from user input

print("This program will output the sum of all the numbers between 1 and whatever you enter into the next line!")

num = getPosInt("Please enter a positive number: ") # calls function imported above
ans = 0 # starts the count at 0

for i in range(1, num+1): # range function will loop from 1 to user inputed value
    ans = ans + i

print (ans)