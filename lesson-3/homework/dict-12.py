given_dict = {
    'car1': 'Matiz',
    'car2': 'Matiz',
    'home': 'Sergeli',
    'phone': 'Xiaomi'
}
value = 'Matiz'

count = list(given_dict.values()).count(value)
print(count)