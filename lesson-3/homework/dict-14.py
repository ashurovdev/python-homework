given_dict = {
    'car1': 'Matiz',
    'car2': 'Matiz',
    'home': 'Sergeli',
    'phone': 'Xiaomi'
}
value = 'Matiz'
new_list = list(key for key in given_dict.keys() if given_dict[key] == value)
print(new_list)