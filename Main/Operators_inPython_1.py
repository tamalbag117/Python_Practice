num1 = int(input("ENTER NO 1 : "))
num2 = int(input("ENTER NO 2 : "))
# Arithmetic operator:
print(num2, "+", num1, "is:", num1 + num2)
print(num2, "-", num1, "is:", num1 - num2)
print(num2, "*", num1, "is:", num1 * num2)
print(num2, "/", num1, "is:", num1 / num2)
print(num2, "//", num1, "is:", num1 // num2)
print(num2, "%", num1, "is:", num1 % num2)
print(num2, "**", num1, "is:", num1 ** num2)  # ** use as num1^num2 like 2^4=16

# Assignment operator
num3 = 10
print(num3)
print(num3 == 10)  # comparison operator
print(num3 == 9)  # comparison operator
num3 += 10
print(num3)
num4 = num3
num3 -= 10
print(num3)
num3 /= 2
print("num3", num3)
print("num4 :", num4)
num4 %= 3
print(num4)
# logical operators
x1 = True
x2 = False
print("AND OPERATOR :", x1, "AND", x2, " return : ", x1 and x2)
print("OR OPERATOR :", x1, "OR", x2, "  return : ", x1 or x2)
# identity operator
print(x1 is not x2)
print(x1 is x2)
# membership operator
my_list_python = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
print("1 is in the list :", 1 in my_list_python)
print("1 is in the list :", 11 in my_list_python)
print("1 is in the list :", 11 not in my_list_python)
# Bitwise operator
print("11 & 12 : ", 11 & 12)
print("11 | 13 :", 11 | 13)







