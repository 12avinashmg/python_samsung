def varLengthArgs(*varArgs):
    print("The user given values are: ")
    print(varArgs)
    for i in varArgs:
        print(i)

varLengthArgs(30, 40, 50, 75, 100)
