# Question 1

num = int(input("Please enter a positive integer: ")) 
ans = 0 # starts the counts at 0
for i in range(1, num+1): # range function will loop from 1 to user inputed value
    ans = ans + i

print (ans)