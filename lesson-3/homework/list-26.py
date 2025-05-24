given_list = [1, 9, 2, -11, 4, 5, 2, 6, 7]
length = len(given_list)
if length%2==1:
    print(f'O\'rtasi: {given_list[length//2]}')
else:
    print(f'O\'rtasi: {given_list[length//2-1]}, {given_list[length//2]}')