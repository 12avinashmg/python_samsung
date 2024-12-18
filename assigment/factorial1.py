# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 20

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
   
elif num == 0 or num == 1:
   print("The factorial is 1")
   
else:
   for i in range(2, num + 1):
       factorial = factorial * i
   print("The factorial of", num, "is", factorial)
