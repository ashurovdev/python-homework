given_dict = {
    'car':'Matiz'
}

given_key = 'car'
if given_key in given_dict.keys():
    value = given_dict.get(given_key)
    print(value)
else:
    print('Key doesn\'t exist')