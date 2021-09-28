# lambda function
cube = lambda x: x*x*x
f_1 = lambda y:y%2 ==0
her_list_1 = [1,2,3,4,5,6,7,8,9]
# map 
print("Cube of the list item : ",list(map(cube,her_list_1)))
#filter
print("Filted List : ",list(filter(f_1,her_list_1)))