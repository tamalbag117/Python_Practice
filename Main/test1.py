def combo(ls, c):
      
    if c == 0:
        return [[]]
      
    l =[]
    for i in range(0, len(ls)):
          
        m = ls[i]
        remLst = ls[i + 1:]
          
        for p in combo(remLst, c-1):
            l.append([m]+p)
              
    return l

a =str("input")
n =int(input("combo :"))
list_1 =[i for i in a]
print("combination :",combo(list_1, n))









