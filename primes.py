# Zoe Cahill - Question 5 Solution

def primenum():
    # Imports a function from PCInput which was created to handle user input
    from PCInput import getPosInt

    # Describes the program to the user
    print("This program will tell you if the number enter is prime or not")

    # Calls the function imported above
    # This function will check that the number entered is a positive integer only
    num = getPosInt("Please enter a positive number: ")

    # Prime numbers must be greater than 1 so we check this with the if statement
    if num > 1:
        # Loops through each number up to num
        for i in range(2, num):
            # Checking if any number in the range above divides into num
            # If true it cannot be a prime number as they can only be divided by themselves and one
            if num % i == 0:
                print (num, "is not a prime number")
                # Terminates current loop and executes next statement once condition is met 
                break
        else:
            # Else means no other number will divide into num so it has to be primes
            print (num, "is a prime number")

    # If input in <= 1 then it cannot be prime
    else:
        print (num, "is not a prime number")

primenum()