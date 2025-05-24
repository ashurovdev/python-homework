def invest(amount, rate, year):
    for i in range(1,year+1):
        amount=amount*(1+rate)
        print(f'year {i}: ${amount:.2f}')
    
invest(100, .05, 4)