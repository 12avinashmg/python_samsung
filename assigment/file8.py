#Program to print the number of words in File

fName = input("Enter the file name: ")
searchLetter = input("Enter the letter to be searched: ")
count = 0

with open(fName, 'r') as fo:  # to do operations on the file
    for line in fo:           # to do operations on each line
        lines = line.split()
        for words in lines:     # split each line into words
            if(words == searchLetter):
                    count = count + 1

print("The number of times ", searchLetter, " appears in file is ", count)
fo.close()
