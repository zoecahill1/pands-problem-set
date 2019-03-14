![Python Banner](/images/python-banner.jpg)
# Problem Set Solutions

This repository contains my solutions to the Problem Set for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)

## How to download this repository

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click to copy the clone URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
7. Press Enter. Your local clone will be created.

## How to run the code

1. Make sure you have python installed
2. Run command line
2. Run start.py 
3. Select which solution you wish to run i.e. enter 1 to start solution 1
4. Alternatively you can run each individual solution by entering python and then its file name 

## What each file contains

1. sumupto.py contains my solution to problem 1 on the problem sheet. It asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
2. begins-with-t.py contains my solution to problem 2 on the problem sheet. It will tell you whether or not today is a day that begins with the letter T
3. divisors.py contains my solution to problem 3 on the problem sheet. It will print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12
4. collatz.py contains my solution to problem 4 on the problem sheet. It will ask the user to input any positive integer and then output the successive values of the following calculation; at each step calculate the next value
by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. The program will then end if the current value is one.
5. primes.py contains my solution to problem 5 on the problem sheet. It will ask the user to input a positive integer and then tell the user whether or not the number is a prime.
6. secondstring.py contains my solution to problem 6 on the problem sheet. It will ask a user to input a sentence and will output every second word
7. squareroot.py contains my solution to problem 7 on the problem sheet. It asks the user to input a positive number and gives the user an approximation of the square root of that number
8. date-time.py contains my solution to problem 8 on the problem sheet. It contains 2 functions one which decides on the suffix to put on the day part of the date and one which prints and formats the current date. It will output todays date in the format   
![Code Example](/images/date-time-example.PNG)  
*note: changed the name specified in the problem sheet from "datetime.py" to "date-time.py" as program kept importing itself rather that the datetime functions needed*
9. second.py contains my solution for problem 9 on the problem sheet. It will read in a text file and output every second line. This program can read a file from your on machine if you input the proper file path.  
*note: there is also a file called moby-dick.txt included here for testing this program simply enter moby-dick.txt when prompted.*
10. plot.py contains my solution to problem 10 on the problem sheet. It will display a plot of the functions x, x^2 and 2^x in the range[0,4]
11. PCInput.py contains the functions used to handle user input. They are in a separate file for reusability

## References
* [The Coder's Apprentice](http://www.spronck.net/pythonbook/index.xhtml) - I used this book in some of my solutions as commented in the code.
* [Stack Overflow](https://stackoverflow.com) - I used Stack Overflow in solution 1 (sumupto.py), as commented in the code
* [Rob Jwells](https://www.robjwells.com/2013/10/date-suffixes-in-python/) - I used this tutorial on date suffixes to fix issue with formatting suffixes of dates in question 8 as commented in code (date-time.py)
* [MatplotLib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) - Referred to throughout my solution in plot.py