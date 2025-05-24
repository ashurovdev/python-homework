given_tuple = (1, 9, 2, -11, 4, 5, 2, 6, 7, 8, 1)
spsnum = 3
sublists= []
for i in range(0, len(given_tuple), spsnum):
    sublists.append(given_tuple[i:i+spsnum])
print(tuple(sublists))