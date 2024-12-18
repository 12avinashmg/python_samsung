
def varLengthArgs(*varArgs):
    print("The user given values are: ")
    print(varArgs)
    for i in varArgs:
        print(i)


varLengthArgs(1, 2, 3)
varLengthArgs(2, 4, 6, 8, 7, 5, 3, 1)
varLengthArgs()

n = int(input("Enter a value for n (n <= 10): "))
list1 = list()  # create a empty list
print("Enter ", n, " numbers: ")
for i in range(n):
    list1.append(int(input()))
    
varLengthArgs(list1)
