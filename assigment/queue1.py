import sys

que = []  # A list is taken as global variable so that it can be
                # accessed in all the functions

def enQueue():
    num = float(input("Enter the element to be inserted:  "))
    que.append(num)  # Add the new element at last of the list

def deQueue():
    if(len(que) == 0):  # check if the list is empty before you pop
        print("The Queue is empty. Cannot delete an element")
        return
    print("The deleted element is ", que[0]) #Display always the 1st element
    que.pop(0) # remove/delete the element from the list
  
def displayQueue():
    if(len(que) == 0):
        print("The Queue is empty")
        return
    print("The Queue elements are: ")
    print(que)

def invalidInput():
    print("Invalid choice entered")

def exitProgram():
    print("End of Program...")
    sys.exit()

choice = 0

queueOperations = {
        1 : enQueue,
        2 : deQueue,
        3 : displayQueue,
        4 : exitProgram
        }

while(True):
    print("\n1:Insert  2:Delete  3:Display Queue  4:Exit Program")
    choice = int(input("Enter your choice: "))
    #stackOperations[choice]()
    queueOperations.get(choice, invalidInput)()
    
print("End of Program")

