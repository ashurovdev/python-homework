def check(a,b):
    if b in a:
        print('Ha')
    else:
        print('yo\'q')

a,b = map(str, input('Kiriting: ').split())
check(a,b)