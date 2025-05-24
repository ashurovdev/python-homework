given_dict = {
    'car1': 'Matiz',
    'car2': 'Matiz',
    'home': 'Sergeli',
    'phone': {
        'Xiaomi':'12 lite'
        }
}
nest = any(isinstance(value, dict) for value in given_dict.values())
print(nest)