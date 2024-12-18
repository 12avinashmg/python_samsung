#!/usr/bin/python

#Program to print a file in terms of words

fName = input("Enter the file name: ")
i = 1
with open(fName, 'r') as fo:  # to do operations on the file
    for line in fo:           # to do operations on each line
        lines = line.split()
        for words in lines:   # to do operations on each word
            print(words)
fo.close()


#Program to print a file in terms of lines
fName = input("Enter the file name: ")
i = 1
with open(fName, 'r') as fo:  # to do operations on the file
    for line in fo:           # to do operations on each line
        lines = line.split()
        i = i + 1
        print("Line-",i,"- ",lines)
fo.close()



# Create a directory "test"
#os.mkdir("test")

