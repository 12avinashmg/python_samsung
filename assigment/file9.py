# Program to copy a file into another line by line

fo1 = open("file1.txt", "r"); # open source file in read mode
fo2 = open("file2.txt", "w"); # open target file in write mode

lineNum = 1 # Line number to be printed on to the Target file

lineText = "  "  # create a string and initialize it

for line in fo1:   # split the file into lines
    lineText = str (lineNum) + "  " # copy the line number to the string
    lineNum = lineNum + 1 # increment line number
    lineText = lineText + line  # Append the text that is read from source
    fo2.write(lineText)   # copy to the text now to the file
    print(lineText)   # print the copied text to the console
    
fo1.close()
fo2.close()
