given_tuple = ('a','b','c')
list1 = list(given_tuple)
number = 4

new_list = [char for char in list1 for i in range(number)]
print(tuple(new_list))