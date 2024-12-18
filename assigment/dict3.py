
dict1 = {'Name': 'Uma', 'Age': 7, 'Class': 'First', 'School': 'Mahaveer'}

dict2 = {'City' : 1, 'State' : 2, 'Country' : 3}

print(dict2['City'], "   ", dict2['State'], "   ", dict2['Country'])

print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])

dict1['Age'] = 8; # update existing entry
dict1['High School'] = "Kaveri School"; # Add new entry

print(type(dict1))

print("\nAfter updation: \n")

print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])
