# List in Python
# from typing import Tuple

name = ["Anirban", "Rangan", "Miko", "UK NK", "Lucifer"]
print(name)
# mixed List
mixing1 = ["ISHITA ROY", 143, 0.99, 'E']
print(mixing1)
print(mixing1[2])
# list shorting
num1 = [2, 5, 78, 3, 88, 23, 1, 94, 33, 21, 5, 3, 67, 27]
print(num1)
num2 = num1.copy()
num1.sort()
print(num1)
num1.reverse()
num1.remove(33)
num1.pop()
num1.append(101)
num1.append(1000)
num1.insert(2, 200000)
print(min(num1))
print(max(num1))

print(num1)
# slicing
print(num2[1:10])
# mutable and immutable
# tuple: immutable
tp: tuple[int, int, int] = (2, 3, 7)
print(tp)
tp1 = (7, 3, 2)
tp3 = tp1 + tp
print(tp3)
# swapping two numbers using python
a = 7
b = 1
a, b = b, a
print(a, b)
print(float(sum(num1)))
