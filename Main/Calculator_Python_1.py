while True:
    # operation +,-,*,,//,**,%
    f = input("Enter operation Type : ")
    num1 = int(input("Enter number one : "))
    num2 = int(input("Enter number two : "))
    if f == "+":
        print(num1, "+", num2, " = ", num2 + num1)
    elif f == "-":
        print(num1, "-", num2, " = ", num2 - num1)
    elif f == "*":
        print(num1, "*", num2, " = ", num2 * num1)
    elif f == "/":
        print(num1, "/", num2, " = ", num2 / num1)
    elif f == "%":
        print(num1, "%", num2, " = ", num2 % num1)
    elif f == "//":
        print(num1, "//", num2, " = ", num2 // num1)
    elif f == "**":
        print(num1, "**", num2, " = ", num2 ** num1)
    else:
        print("Thanks")
        exit(1)
