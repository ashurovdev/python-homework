given_dict = {
    'car1': 'Matiz',
    'car2': 'Matiz',
    'aome': 'Sergeli',
    'phone': 'Xiaomi'
}

new_dict = {key:value for key,value in sorted(given_dict.items(), key=lambda x: x[1])}
print(new_dict)