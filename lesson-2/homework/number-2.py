numbers = list(map(float, input('3 ta raqam kiriting: ').split()))
numbers.sort()
print(f'Max = {numbers[-1]} \nMin = {numbers[0]}')