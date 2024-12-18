

num = int (input("Enter a number to find if it is a Perfect square:"))

root = int (num ** 0.5)

if(root * root == num):
    print("The number ", num, " is a Perfect square")
else:
    print("The number ", num, " is not a Perfect square")
    

