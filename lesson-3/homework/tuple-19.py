given_tuple = ('a','abs','thdd', 'jh','a')
elem = 'a'
list1 = list(given_tuple)
if elem in list1:
    list1.remove(elem)

print(tuple(list1))