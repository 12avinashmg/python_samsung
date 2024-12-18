def push():
    print("An element is Pushed"),

def pop():
    print("Popped an element"),

def displayStack():
    print("The stack elements are: ")

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
