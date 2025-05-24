volwes = 'aeiouAEIOU'
txt = input('Matnni kiriting: ')
print(f'{"".join("*" if char in volwes else char for char in txt)}')