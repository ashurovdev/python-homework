import random

choice = ['rock', 'paper', 'scissors']

user_score = 0 
bot_score = 0

while True:    
    if user_score==5:
        print('You win, great')
        break
    elif bot_score==5:
        print('You lose, sorry(')
        break
    else:
        try:
            user = int(input('Enter number: Rock is 1 , Paper is 2, Scissors is 3 '))
            if not user in [1,2,3]:
                print('You entered wrong. Please enter 1, 2, 3')
                continue
        except:
            print('You entered wrong. Please enter 1, 2, 3')
            continue
        random_choice = random.choice(choice)
        user = choice[user-1]
        if random_choice==user:
            print('Draw')
        elif (random_choice=='rock' and user=='paper') or (random_choice=='paper' and user=='scissors') or (random_choice=='scissors' and user=='rock'):
            print('You +1')
            user_score+=1
        else:
            print('Bot +1')
            bot_score+=1
    print(f'Your score: {user_score} and bot score: {bot_score}')