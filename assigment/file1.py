#!/usr/bin/python

# Open a file
fo = open("list3.py", "r")
print ("Name of the file: ", fo.name)
print ("File Closed ? : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
print ("File Closed? : ", fo.closed)
#print ("Softspace flag : ", fo.softspace)


#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)

# Close opend file
fo.close()

