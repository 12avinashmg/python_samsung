
stk = []  # A list is taken as global variable so that it can be
                # accessed in all the functions

stkSize = int(input("Enter size of the stack: "))

def push(sp):
    if(sp == stkSize):
        print("Stack is full. Cannot push an element")
        return sp
    
    num = int(input("Enter the element is Pushed:  "))
    stk.append(num)  # Add the new element at last of the list
    sp = sp + 1
    return sp

def pop(sp):
    if(len(stk) == 0):  # check if the list is empty before you pop
        print("The stack is empty. Cannot pop an element")
        return sp
    print("The popped element is ", stk.pop()) # pop() removes the top ele
    sp = sp - 1
    return sp
  
def displayStack(sp):
    if(sp == 0):
        print("The stack is empty")
        return sp
    print("The stack elements are:  ")
    for i in  range(0, sp):
        print(stk[i], "  ")
    return sp

def invalidInput(dummyVariable):
    print("Invalid choice entered")

stackOperations = {
        1 : push,
        2 : pop,
        3 : displayStack 
        }

choice = 0
stkPointer = int (0)

while(True):
    print("1:Push  2:Pop  3:Display Stack")
    choice = int(input("Enter your choice: "))
    #stackOperations[choice]()
    stkPointer = stackOperations.get(choice, invalidInput)(stkPointer)
    choice = int(input("Do you wish to Exit? (Yes-1):  "))
    if(choice == 1):
        break

print("End of Program")
