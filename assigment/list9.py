my_list = ['p','r','o','b','l','e','m']
print(my_list)

my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
#print(my_list)

# Output: 'r'
print(my_list.pop())

#print(my_list)

# Output: ['r', 'b', 'l', 'e', 'm']
#print(my_list)

# Output: 'm'
print(my_list.pop())
print(my_list)

print(my_list.pop())
print(my_list)

# Output: ['r', 'b', 'l', 'e']
#print(my_list)

my_list.clear()

# Output: []
print(my_list)

del my_list

my_list.append('Blr') # ERROR  cannot add/append elements to
my_list.append('Mys')  # non-existing list
my_list.append('Hubli')

print(my_list) # Error my_list does not exist
