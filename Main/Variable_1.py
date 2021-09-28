print("variable ans datatype")
a1 = "is"
a2 = "are"
a3 = 35.7
a4 = 44.9
a5 = 90
"""
print(a1 + a2)
print(type(a1 + a2))
print(a3 + a4)
print(type(a3 + a4))
print(type(a5))
print(int(a3))
print(str(a4))
# multiple print
print(10 * "****\n")
# User input
print("Enter name:")
a6 = input()
print("you have entered :", a6)
print("Enter number:")
a7=input()
print(int(a7)+12)
"""
# strings in python
print("your name")

herName = input()
print("Her name is : ", herName)
print(len(herName))
print(herName[0:7])
print(herName[0:len(herName)])
# slicing
print(herName[0:10:3])
print(herName[::-2])
# alpha numeric string
print(herName.isalnum())
print(herName.endswith("ROY"))
# count number of element in a string
print(herName.count("I"))
print(herName.count("A"))
# search
print(herName.find("ROY"))
# to lower case
print(herName.lower())
print(herName.replace("ISHITA", "TOUKA"))
