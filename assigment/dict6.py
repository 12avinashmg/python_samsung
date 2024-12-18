my_dict = {'name':'Jack', 'age': 26, 10 : 10}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
print(my_dict.get('address'))
print(my_dict.get(10))
# my_dict['address']
