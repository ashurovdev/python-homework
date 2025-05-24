def factor(number):
    print(f'1 is a factor of {number}')
    for i in range(2,number//2+1):
        if number % i == 0:
            print(f'{i} is a factor of {number}')
    print(f'{number} is a factor of {number}')

number = int(input('Enter a positive integer: '))
factor(number)