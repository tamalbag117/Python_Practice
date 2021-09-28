# File io Basics
# r -----> reading file
# w -----> writing in file
# x -----> creates fil;e if not exists
# a -----> Add more content to a file
# t -----> open file in text mode
# b -----> open file in binary mode
# + -----> read and write mode
"""
f1 = open("name.txt", "rt")
f2 = f1.read()
print(f2)
f1.close()
"""
f2 = open("name.txt", "a")
f3 = f2.write("how are you, dear\n nice to meet you")
print(f3)  # print number of character
f2.close()



