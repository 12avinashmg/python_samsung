def findSumOfNumbers(list1):	#finding the sum using built in method
    return (sum(list1))

def findSumOfNumbers1(list2):	#finding the sum by iterating the list
  sumOfNums = 0
  for i in list2:
    sumOfNums = sumOfNums + i
  return sumOfNums

def findSumOfSquares(list1):	#storing numbers in a new list, then finding sum
    list2 = []
    for i in list1:
        list2.append(i ** 2)
    return (sum(list2))

def findSumOfSquares1(list1):	#iterating the list to find the sum
    sumOfSqrs = 0
    for i in range(len(list1)):
        sumOfSqrs = sumOfSqrs + (list1[i] ** 2)
    return sumOfSqrs

n = int(input("Enter a value for n (n <= 10): "))
print("Enter ", n, " numbers: ")
a = []
for x in range(0, n):
    a.append(int(input()))

choice = int(input("Enter your choice: "))
if(choice == 1):
    sumOfNumbers = findSumOfNumbers1(a)
    print("The sum of the numbers is: ", sumOfNumbers)
else:
    sumOfNumbers = findSumOfSquares(a)
    print("The sum of Squares of the numbers is: ", sumOfNumbers)

