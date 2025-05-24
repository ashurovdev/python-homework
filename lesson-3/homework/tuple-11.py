given_tuple = (1, 9, 2, -11, 4, 5, 2, 6, 7, 8, 1)
elem = 2
index_list = []
for i in range(0, len(given_tuple)-1):
    if given_tuple[i]==elem:
        index_list.append(i)

print(index_list)