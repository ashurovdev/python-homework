given_dict1 = {
    'car': 'Matiz',
    'home': 'Sergeli',
    'phone': 'Xiaomi'
}
key = 'home'
if key in given_dict1.keys():
    given_dict1.pop(key)
    print(given_dict1)
