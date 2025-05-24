txt = input('Matnni kiriting: ')
check_dig = any(let.isdigit() for let in txt)
if check_dig:
    print('Raqam mavjud')
else:
    print('Raqam mavjud emas')