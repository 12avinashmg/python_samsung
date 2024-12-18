# initialize A and B
A = {1, 2, 3, 4, 5, 6, 10}
B = {4, 5, 6, 7, 8, 9, 10}
C = {7, 9, 11, 10, 6}
print("SEt A = ", A)
print("Union of all 2 sets A, B: ",A | B)

l1 = []  # create an empty list

l1 = A & B # copy the common elements to be deleted into the list

print(l1) # Print the list

for i in l1:   # Run through the list
    A.discard(i)   # discard the elements from set A by specifying the
                            # elements from the list

print(A)  # Lastly print the set A



E = (A & B & C)
print("Common elements of sets A, B, E: ", E)

E = A & B

A = (A - E)
print("After removing common elements from set A:", A)




# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
#print(A ^ B)

#1.Create 3 sets print all the elements of the 3 sets without repetition

#2.Remove the elements that are common between A and B, from set A

#3.Add only the common elements in A and B in C

