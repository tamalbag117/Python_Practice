# User define Function
def function_1(c, d):
    av = round(sum((c, d))/2)
    print("hello function ;", av)


def function_2(c1, c2):
    return c1-c2


def function_3():
    """This is a Function prototype in Python"""
    print("Printing Docs String")
    return 0


a = int(input("Enter number one : "))
b = int(input("Enter number two : "))
print(function_1(a, b))
print(function_2(a, b))
print(function_3.__doc__)
