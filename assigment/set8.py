# initialize A and B
A = {1, 2, 3, 4, 5, 8, 4}
B = {4, 5, 6, 7, 8, 3, 5}

# use & operator
# Output: {4, 5}
print(A & B)  # Intersection of 2 sets


C = A | B
print(C)

D = A | C & B
print(D)
