given_tuple = ('a','jh','thdd', 'jh','a')
given_list = list(given_tuple)
new_list = []
for char in given_list:
    if char in new_list:
        pass
    else:
        new_list.append(char)

print(tuple(new_list))