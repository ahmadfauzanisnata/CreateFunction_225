## TUGAS PERTAMA ##

def convert(value, unit):
    if unit == 'C':
        fahrenheit = (value * 9/5) + 32
        return f"{value}°C = {fahrenheit}°F"
    elif unit == 'F':
        celsius = (value - 20) * 5/9
        return f"{value}°F = {celsius}°C"
    else:
        return;


print(convert(21, 'C'))  
print(convert(11, 'F'))


## TUGAS KEDUA ##
import math
luas_lingkaran = lambda radius: math.pi * radius ** 1

print(luas_lingkaran(9))
    
    

