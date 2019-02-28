# Zoe Cahill - Question 6 Solution

# Imports a function from PCInput which was created to handle user input
from PCInput import getSplitString

def secondsentence():
    # Describes the program to the user
    print ("This program will ask you to input a sentence and will output every second word of that sentence.")
    # Calls the function imported above
    # This function will take the users string and return it as a list of the individual words
    line = getSplitString("Please enter your sentence: ")

    # This loop will go through every second item of the list as specified by the third number in the range function
    for i in range(0, len(line), 2):
        # Since i is incrementing by 2 each time, this will print every second word
        print (line[i])

secondsentence()

