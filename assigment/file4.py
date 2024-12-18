#!/usr/bin/python

# Open a file
fo = open("list8.py", "r+")
str1 = fo.read(10);
print ("Read String is : ", str1)

# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str1 = fo.read(10);
print ("Again read String is : ", str1)
# Close opend file
fo.close()
