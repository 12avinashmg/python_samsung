def defArgFunc( empname = "Raam", emprole = "Manager" ):   
   print ("Emp Name: ", empname, end=", ")
   print ("Emp Role: ", emprole)


defArgFunc("Something", "  ", emprole = "Programmer")

print("\n************************")
print("Both default values will be used:")
defArgFunc()

print("\n************************")
print("Using the default value for Name:")
defArgFunc(emprole = "Programmer")
defArgFunc("Programmer")


print("\n************************")
print("Over-riding both the default values:")
defArgFunc(empname="Hari", emprole = "CEO")

defArgFunc(emprole = "CTO", empname = "Krishna")

defArgFunc("Manager", "Dhanuja")
