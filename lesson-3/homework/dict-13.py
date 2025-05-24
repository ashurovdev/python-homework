given_dict = {
    'car1': 'Matiz1',
    'car2': 'Matiz',
    'home': 'Sergeli',
    'phone': 'Xiaomi'
}

new_dict = {value:key for key, value in given_dict.items()}
print(new_dict)