# Built in functions
# abs() returns absolute value
print(abs(12.3))
print(abs(-90.6))
# all function return true if all element are iterable
iterable_checking_list = (1, 2, 3, 4, 5, 6)
iterable_checking_list_1 = [1, 8, 5, 4, 5, 6]
print(all(iterable_checking_list))
print(all(iterable_checking_list_1))
print(all([int(11), int, int]))
# bin : convert decimal to binary
print(bin(12))
# bool : return boolean
x1 = 1
x2 = 0
print(bool(x1 & x2))
print(bool(x1 | x2))
# chr(i) : return  character from unicode
print(chr(90))
print(chr(8364))
# divmod
print(divmod(100, 45))
print(divmod(100.00, 45.03))
# enumerate
checking_list_obj_1 = [10, 2, 3, 4, 5, 6, 7, 8]
print(list(enumerate(checking_list_obj_1, start=11)))
# eval
print(eval('checking_list_obj_1[4]+2'))  # index=4 , present element 5 so 5+2==7
print(hash(2.8))  # return hash value
# hex : convert number to hexadecimal number
print(hex(143))
# len : return length of a object
print(len(checking_list_obj_1))
# max return maximum among , min return minimum number
print(max(1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 7))
print(min(1.1111111, 5.666666, 23456.78, 0.34))
# ord return unicode
print(ord('w'))
print(round(12.3))
print(round(12.5))
print(round(12.7))
print(iterable_checking_list_1)
print(sorted(iterable_checking_list_1))
print(sum(iterable_checking_list_1))
x1 = 9
x2 = 1
print(sum((11, 1)))
print(sum((x1, x2)))
exit(1)
