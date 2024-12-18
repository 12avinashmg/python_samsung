#!/usr/bin/python

# Open a file
fo = open("list3.py", "r+") #opening the file in read and write mode
str = fo.read(25);
print ("Read String is : ", str)
# Close opend file
fo.close()


read()  // reads a word
read(1)  reads a character
readline()  reads a line
readline(40)  reads one line or max 40 chars in a line
readlines(20)  reads 20 lines of text from the file





