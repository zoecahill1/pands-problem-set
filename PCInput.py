#  Zoe Cahill - Contains functions which handle user input
# Adapted from Coder's Apprentice Appendix C

# Defines the function - This will check users has inputted positive numbers only
def getPosInt(x):
    # Will keep looping until we meet condition
    # Used as we do not know how many tries user will need to input correct data
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

# Defines the function - This function will take a user inputted string and return it as a list of words
def getSplitString(x):
    # This line gets the users input
    line = input(x)
    # This returns the string seperated by white spaces as a list ie "Hello world" becomes ["Hello", "world"]
    return line.split()

# Defines the function - This function will check user has inputted a positive number only 
# and will make sure it is returning float type
def getFloat(x):
    # Will keep looping until we meet condition
    # Used to keep asking for user input until condition is met
    while True:
        # Testing to see if input is number - if int will make into float
        try:
            num = float(input(x))
        # Will catch error if user inputs something that is not a number
        except ValueError:
            print( "That is not a number -- please try again" )
            # Returns control to beginning of while loop to check next input
            continue
        # When checks are passed returns float to program
        return num

# Defines the function - This function will try to open a file path that the user has inputted
# If it cannot open it will show an error message to the user with direction on how to input file path
def fileCheck(x):
    # Will keep looping until we reach condition
    # User will be asked to keep inputting file path until it can be opened
    while True:
        # This line gets the users input
        filename = input (x)
        # This will attempt to open the file in read only mode
        try:
            file1 = open (filename, "r")
        # If error eg file path not found user will be shown a message with directions to fix
        except OSError:
            # Tells the user what filename it was trying to open
            print ("Could not read file: ", filename)
            # Gives the user some guidance on how to format file path
            print ("Please enter in format filename.txt if file is in this folder")
            print ("If file is elsewhere then specify file path for example if file is on desktop C:\\Users\\User\\Desktop\\filename.txt")
            # Returns control to beginning of loop to check next input
            continue
        # Returns file path to main program if it passes checks
        return file1