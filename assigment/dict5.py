# empty dictionary
my_dict = {}
#my_dict = dict()

# dictionary with integer keys
my_dict = {3: 'apple', 2: 'apple', 1:'Mango'}

my_dict[1] = 'Pineapple' # to change the value of a key in a dictionary
print(my_dict)
del(my_dict[1])  # to delete a value in a dictionary

print(my_dict)

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict['name'][2])

# using dict()
my_dict3 = dict({1:'apple', 2:'ball'})
print(my_dict3)
# from sequence having each item as a pair
my_dict1 = dict([(1,'apple'), (2,'ball')])
print(my_dict1)

"""
C/C++
msdn
docs.microsoft.com

Java
docs.oracle.com

Python
python.org

List (vector and list of C++)
Implicitly it is like Dynamic Array
Random Acces is pissible
Sortable
dynamically grows and shrinks
General purpose and most widely used DS in Python

set
unordered
Associative DS
faster compared to list
unique elements
mathematical oprs such as union, intersect etc

Dict
unordered map
impliciltly a pair
key/value pairs (where keys are unique)

tuple
ordered list
Immutable (cannot add/change data)
vary fast in oprs
"""
