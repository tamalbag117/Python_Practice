my_list_1 = []
i = 0
while i <20:
    my_list_1.append(int(input("Enter Number --->")))
    i+=1
print("myList: ",my_list_1)
my_even_list =[i for i in my_list_1 if i%2==0]
print("Event list series :",my_even_list)
print("Total number of even numbers in the list :",len(my_even_list))
my_odd_list = [i for i in my_list_1 if i not in my_even_list]
print("odd list series :",my_odd_list)
print("Total number of odd numbers in the list :",len(my_odd_list))

