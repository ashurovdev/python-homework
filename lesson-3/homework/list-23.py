given_list = [1, 9, 2, -11, 4, 5, 2, 6, 7]
new_list = []
for char in given_list:
    if char%2==1:
        new_list.append(char)

print(new_list)