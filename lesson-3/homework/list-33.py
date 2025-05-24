given_list = [1, 9, 2, -11, 4, 5, 2, 6, 7]
elem = 2
index_list = []
for i in range(0, len(given_list)-1):
    if given_list[i]==elem:
        index_list.append(i)

print(index_list)