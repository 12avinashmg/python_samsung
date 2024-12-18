
def findSum(varArgs):   # this function can take any No. of args
    return (sum(varArgs))
    
print("\nEnter few numbers seperating them with space: ")
a = [int(x) for x in input().split(',')] # a here is a list

print(a)
sumOfNums = findSum(a)
print("Sum of the numbers = ", sumOfNums) #sum(a)
print("Number of elements in the list is ", len(a))

#sumOfNums = 0
 #   for i in varArgs:
  #      sumOfNums = sumOfNums + i
   # print("Sum of the numbers = ", sumOfNums)
