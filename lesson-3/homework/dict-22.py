dict1 = {'a':1, 'b':2, 'c':3}
new_dict = {key:value for key, value in dict1.items() if value>1}
print(new_dict)