import sys

que = []  # A list is taken as global variable so that it can be
                # accessed in all the functions

qSize = int(input("Enter size of the Queue: "))

def enQueue(rp):
    print("Queue size = ",qSize)
    if(rp == qSize):
        print("Queue is full")
        return rp
    
    num = input("Enter the element to be inserted:  ")
    que.append(num)  # Add the new element at last of the list
    rp = rp + 1
    return rp

def deQueue(rp):
    if(len(que) == 0):  # check if the list is empty before you pop
        print("The Queue is empty. Cannot delete an element")
        return rp
    print("The deleted element is ", que[0]) #Display always the 1st element
    que.pop(0) # remove/delete the element from the list
    rp = rp - 1
    return rp
  
def displayQueue(rp):
    if(len(que) == 0):
        print("The Queue is empty")
        return
    print("The Queue elements are: ")
    print(que)

def invalidInput(rp):
    print("Invalid choice entered")

def exitProgram(rp):
    print("End of Program...")
    sys.exit()

choice = int(0)

queueOperations = {
        1 : enQueue,
        2 : deQueue,
        3 : displayQueue,
        4 : exitProgram
        }

rearPointer = int(0)

while(True):
    print("\n1:Insert  2:Delete  3:Display Queue  4:Exit Program")
    choice = int(input("Enter your choice: "))
    #stackOperations[choice]()
    rearPointer = queueOperations.get(choice, invalidInput)(rearPointer)
    
print("End of Program")

