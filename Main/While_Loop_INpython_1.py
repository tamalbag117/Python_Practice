flag = int(input("Enter a number:"))
while True:
    if flag > 37:
        break
    if flag > 30:
        continue
    print(flag)
    flag = flag + 7

