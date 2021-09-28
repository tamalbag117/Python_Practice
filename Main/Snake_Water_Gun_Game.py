import random
def game_snake(c,u):
    if c==u:
        return None
    elif c=='s':
       if u=='w':
           return False
       elif u=='g':
           return True
    elif c =='w':
        if u =='g':
            return False
        elif u =='s':
            return True
    elif c =='g':
        if u =='s':
            return False
        elif u=='w':
            return True
    
computer_1 = print("Computer's turn :chose ----> snake(s) water(w) or gun(g)  : #")
randomNum = random.randint(1, 3)
if randomNum ==1:
    computer_1 = 's'
elif randomNum == 2:
    computer_1 ='w'
elif randomNum == 3:
    computer_1 ='g'
player_1 = input("your's turn :chose ----> snake(s) water(w) or gun(g)   :")
q = game_snake(computer_1,player_1)
print(f"Computer chose   :{computer_1} , you chose :{player_1}")
if q==None:
    print("It's a tie !")
elif q:
    print("congratulation! you won")
else:
    print("sorry for your loss")



