given_dict = {
    'car1': 'Matiz',
    'car2': 'Matiz',
    'aome': 'Sergeli',
    'phone': 'Xiaomi'
}

new_dict = {key: given_dict[key] for key in sorted(given_dict)}
print(new_dict)