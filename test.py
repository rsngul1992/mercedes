# Python program to find the factorial of a number provided by the user.

# change the value for a different result
number = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if number < 0:
   print(" factorial do  not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("The factorial of",number, "is",factorial)
