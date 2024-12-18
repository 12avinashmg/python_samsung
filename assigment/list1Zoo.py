# These list elements are all of the same type
zoo = ['bear', 'lion', 'panda', 'zebra']
print(zoo)

print(zoo[0])

# But these list elements are not
biggerZoo = ['bear', 'lion', 'panda', 'zebra', ['chimpanzees', 'gorillas', 'orangutans', 'gibbons']]
print(biggerZoo)

print(biggerZoo[1])

print(biggerZoo[3])

print(biggerZoo[4])

print(biggerZoo[4][0])

print(biggerZoo[4][0][1])
