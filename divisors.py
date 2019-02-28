# Zoe Cahill - Question 3 Solution

def divideby():
    # This print statement describes the program to the user
    print ("This program prints all numbers between  1,000 and 10,000 that are divisible by 6 but not by 12.")
    
    # Use for loop and range function to iterate through 1000 to 10000 and test one by one
    for i in range (1000, 10000):
        # If checks if number is divisible by 6 (there will be no remainder) 
        # AND if it is not divisible by 12 (there will be a remainder ie not zero)
        if i%6 == 0 and i%12 !=0:
            # If both of these statements are true then print the number
            print (i)

divideby()