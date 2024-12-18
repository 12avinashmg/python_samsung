def zero(n):
    print ("You typed zero.\n")
 
def sqr(n):
    print (n, " is a perfect square\n")
 
def even(n):
    print ("n is an even number\n")
 
def prime(n):
    print ("n is a prime number\n")

def invalidInput(n):
    print("Invalid choice entered")
    
options = {
                0 : zero,
                1 : sqr,
                4 : sqr,
                9 : sqr,
                2 : even,
                3 : prime,
                5 : prime,
                7 : prime,
}

num = 90
options.get(num, invalidInput)(num)

#options[num](num)

