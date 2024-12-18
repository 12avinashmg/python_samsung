
n = int (input("Enter  value for 'n': ") )

m = int(input("Enter number of terms of the series: ") )

sum = 0.0;

for i in range(0, m):
    sum = sum + (n ** i) * ((-1)** i)

print("Sum of the series is ", sum)

1 - n + n2 - n3 + n4 .... up to m terms


