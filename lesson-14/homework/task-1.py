import numpy as np

fah = np.array([32, 68, 100, 212, 77])
@np.vectorize
def fahrenheit2celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit2celsius(fah))