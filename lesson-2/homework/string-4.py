txt = input('Matnni kiriting: ')
txt_m = txt[::-1]
if txt == txt_m:
    print('Palindrom')
else:
    print('Palindrom emas')