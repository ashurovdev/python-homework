txt = input('Matnni kiriting: ')
vowels = txt.count('a')+txt.count('e')+txt.count('i')+txt.count('o')+txt.count('u')+txt.count('o\'')
space = txt.count(' ')
print(f'Unli harflar: {vowels} \nUndosh harflar: {len(txt)-vowels-space}')