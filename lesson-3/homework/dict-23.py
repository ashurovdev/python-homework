dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'b':3,'h':2}
keys = set(dict1.keys()).intersection(set(dict2.keys()))
print(keys)
