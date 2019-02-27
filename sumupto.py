# Zoe Cahill -  Question 1 Solution

def sum():
    # Imports a function from PCInput which was created to handle user input
    from PCInput import getPosInt 

    # Describes the program to the user
    print("This program will output the sum of all the numbers between 1 whatever you choose")

    # Calls the function imported above
    # This function will check that the number entered is a positive integer only
    num = getPosInt("Please enter a positive number: ")

    # Made code more efficient by removing for loop
    # Adapted from stack overflow see below for original loop
    sum = ((num * (num+1))/2)

    #for i in range(1, num+1):
    #sum = sum + i

    # Print out the sum of all the numbers
    print (int(sum))

sum()