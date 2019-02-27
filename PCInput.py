#  Zoe Cahill - Contains functions which handle user input
# Adapted from Coder's Apprentice Appendix C

# Defines the function
def getPosInt(x):
    while True:
        try:
            # Testing to see if number is an int
            num = int(input(x)) 
            # Testing for negatives and zero entries
            if num <= 0: 
                # What is shown to user if they enter 0 or a negative value
                print ("You can only enter positive numbers...Please try again")
                # Returns control to beginning of while loop to check next input
                continue
            # Terminates current loop and executes next statement once condition is met    
            break 
        # Will catch error if user inputs something that is not an int
        except ValueError: 
            print("You can only enter integers...Please try again")
            # Returns control to the beginning of while loop to check next input
            continue
    # Returns the number if it passes above checks to main program
    return num

# Defines the function
def getSplitString(x):
    # This line gets the users input
    line = input(x)
    # This returns the string seperated by white spaces as a list ie "Hello world" becomes ["Hello", "world"]
    return line.split()