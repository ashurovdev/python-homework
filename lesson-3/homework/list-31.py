given_list = ['a', 'absd', 'gh', 'uyt']
number = 4

new_list = [char for char in given_list for i in range(number)]
print(new_list)