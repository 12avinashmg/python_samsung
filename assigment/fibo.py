
fNum = int (input("Enter the 1st number of the series: ") )

sNum = int (input("Enter the 2nd number of the series: ") )

noOfTerms = int (input("Enter number of terms of the series: ") )

print("The Fibonacci series is: \n", fNum, "\n", sNum)

for i in range(3, noOfTerms + 1):
    tNum = fNum + sNum
    print(tNum)
    fNum = sNum
    sNum = tNum
    
