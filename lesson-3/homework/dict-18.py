given_dict = {
    'car1': 'Matiz',
    'car2': 'Matiz',
    'home': 'Sergeli',
    'phone': {
        'Xiaomi':'12 lite'
        }
}
value = 'car'
if given_dict.get(value, False):
    print(given_dict[value])
else:
    print('Default answer')
