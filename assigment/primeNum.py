

num = int(input("Enter the number to find if it is Prime number: "))
flag = 1

if(num == 0) or (num == 1):
    printf("The number is not a prime number")
else:
    for i in range(2, num // 2):
        if(num % i == 0):
            print("The number", num, " is not a Prime number")
            flag = 0
            break;

if(flag == 1):
    print("The number", num, " is a Prime number")
