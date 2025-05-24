def convert_cel_to_far(celsi: float):
    faren = celsi*(9/5)+32
    return faren

def convert_far_to_cel(faren: float):
    celsi = (faren-32)*(5/9)
    return celsi

faren = float(input('Enter a temperature in degrees F: '))
print(f'{faren} degrees F = {convert_far_to_cel(faren):.2f} degrees C')

celsi = float(input('Enter a temperature in degrees C: '))
print(f'{celsi} degrees C = {convert_cel_to_far(celsi):.2f} defrees F')