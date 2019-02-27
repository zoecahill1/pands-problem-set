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
4. Alternatively you can run each individual solution by entering its file name 

## What each file contains

1. start.py contains a menu which will allow you to call the various solutions to each problem. They are numbered as per the question sheet.
2. sumupto.py contains my solution to problem 1 on the problem sheet. It asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
3. begins-with-t.py contains my solution to problem 2 on the problem sheet. It will tell you whether or not today is a day that begins with the letter T
4. divisors.py contains my solution to problem 3 on the problem sheet. It will print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12
5. collatz.py contains my solution to problem 4 on the problem sheet. It will ask the user to input any positive integer and then output the successive values of the following calculation; at each step calculate the next value
by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. The program will then end if the current value is one.
6. primes.py contains my solution to problem 5 on the problem sheet. It will ask the user to input a positive integer and then tell the user whether or not the number is a prime.

12. PCInput.py contains the functions used to handle user input. They are in a separate file for reusability

## References
[The Coder's Apprentice](http://www.spronck.net/pythonbook/index.xhtml) - I used this book in some of my solutions as commented in the code.
[Stack Overflow](https://stackoverflow.com) - I used Stack Overflow in solution 1, as commented in the code