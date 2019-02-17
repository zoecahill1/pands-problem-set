def getPosInt(x):
    while True:
        try:
            num = int(input(x)) # testing to see if number is an int
            if num <= 0: # testing for negatives and zero entries
                print ("You can only enter positive numbers...Please try again")
                continue
            break
        except ValueError: # will catch error if user inputs something that is not an int
            print("You can only enter integers...Please try again")
            continue
    return num