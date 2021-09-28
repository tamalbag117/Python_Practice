import random
ran_dom_1 = random.randint(1,100)
g_s = 0
user_Guess_1 = None
while user_Guess_1 != ran_dom_1 :
   user_Guess_1 = int(input("What is your guess ?\nEnter your guess:"))
   g_s += 1
   if(user_Guess_1 == ran_dom_1):
      print("Your gess is right !")
   else:
      if user_Guess_1 > ran_dom_1:
          print("wrong guess ! try to enter smaller number")
      else:
          print("wrong guess ! try to guess larger number")

print(f"You gess the number in {g_s}  guesses")