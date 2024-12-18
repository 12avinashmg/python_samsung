
stk = []  # A list is taken as global variable so that it can be
                # accessed in all the functions

def push():
    num = int(input("Enter the element is Pushed:  "))
    stk.append(num)  # Add the new element at last of the list

def pop():
    if(len(stk) == 0):  # check if the list is empty before you pop
        print("The stack is empty. Cannot pop an element")
        return
    print("The popped element is ", stk.pop()) # pop() removes the top ele
  
def displayStack():
    if(len(stk) == 0):
        print("The stack is empty")
        return
    print("The stack elements are: ")
    print(stk)

def invalidInput():
    print("Invalid choice entered")

choice = 0

stackOperations = {
        1 : push,
        2 : pop,
        3 : displayStack 
        }

while(True):
    print("1:Push  2:Pop  3:Display Stack")
    choice = int(input("Enter your choice: "))
    #stackOperations[choice]()
    stackOperations.get(choice, invalidInput)()
    choice = int(input("Do you wish to Exit? (Yes-1):  "))
    if(choice == 1):
        break

print("End of Program")
