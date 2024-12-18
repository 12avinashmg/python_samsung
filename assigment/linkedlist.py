class Node:
    def __init__(self, value = None, next = None):
        self.value = value;
        self.next = next;
				
class LinkedList:

    def __init__(self):
        self.head = None;
        self.size = 0;

    def insert(self, item): # add the new node as 1st node in the list
       curr = Node();  # create a new node
       curr.value = item #add the user given value as data of new node 
       self.size += 1   # increment the no. of nodes in the head node
       if(self.head == None):   #check if the list is empty
            self.head = curr
       else:
            curr.next = self.head  # add the id of 1st node as link
			                         of new node
            self.head = curr  # add the id of new node as 1st node

    def remove(self, item): #deletes the last node in the list 
        if(self.head == None): #check if list is empty
             raise Exception('Removing from an empty list')
        curr = self.head  # a new temp-var points to the 1st node
       if(curr.value == item): # serach if the current node is key-node
            self.head = curr.next # if yes, make the 2nd node as 1st
            return   # and return
        while(curr.next.value != item):  #traverse the linked list
            curr = curr.next #jump to the next node
       if(curr.next == None):  #chexk if the current node to b deleted
            raise Exception('Item not present in list')
        else:
            curr.next = curr.next.next #delete the node that was found

    def print_list(self):
        curr = self.head;
        while(curr):
            print(curr.value, end=' ')
            curr = curr.next
			
list = LinkedList()
list.insert(2)
list.insert(5)
list.remove(2)