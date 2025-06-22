import numpy as np

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

@np.vectorize
def number_pow(number, power):
    return (number**power)

print(number_pow(numbers, powers))