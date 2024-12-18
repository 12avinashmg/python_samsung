# program to reverse a number

n = int(input("Enter the number to reverse: "))
rev = 0
temp = n
while(n > 0):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse of the number:",rev)
if (rev == temp):
    print("The number ",temp, " is a Palindrome")
else:
    print("The number ",temp, " is not a Palindrome")

Find the sum of digits of a number
Find the smallest or Biggest digit in a number
Count the number of Even/Odd digits in a number
* Count the number of Prime digits in an number





