import random
a = 0 
rest = ['Y','YES', 'y', 'yes', 'ok']
random_number = random.randint(1,100)
while a<11:
    answer = input('Answer? ')
    if answer in rest:
        random_number = random.randint(1,100)
        a = 0
        print('Restarted')
    else:
        try:
            if int(answer)==random_number:
                print('You guessed it right!')
                break
            elif int(answer)>random_number:
                print('Too high!')
            elif int(answer)<random_number:
                print('Too low!')
            a+=1
            if a==10:
                print('You lost. Want to play again? ')
                print(f'{random_number}')
        except:
            print('You entered wrong!')