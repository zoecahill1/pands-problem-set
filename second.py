# Zoe Cahill - Question 9 - Solution

# Imports a function from PCInput to handle user input and errors
from PCInput import fileCheck

def second():
    # file 1 will call fileCheck() and take on the result after it has been verifed as a correct file path
    file1 = fileCheck("Enter file path: ")
    # readlines() will read each line in the txt file and put put it as a string into the list L
    L = file1.readlines()

    # This for loop through the list from [0] to how ever many lines are in the list L in increments of 2
    for i in range (0, len(L), 2):
        # This will print every second item in the list as we have specified increments of 2 above
        print (L[i])

second()


