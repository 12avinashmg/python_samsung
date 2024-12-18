# Program to print the Lucky number
def findSum(n) :
    while n >= 10 :   # until the number is not a single digit number
        sum = 0
        while n != 0 :
            sum = sum + n % 10
            n = n // 10
        n = sum
    return sum

n = int(input("Enter a number to find sum of its digits: "))
m = findSum(n)
print("Sum of the digits = ", m)
