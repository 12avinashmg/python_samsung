# mistake values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[:-3] = [10, 20, 30, 40]  

# Output: [1, 3, 5, 7, 10 ,20]
print(odd)   
