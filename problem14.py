import math
num = int(input("Enter number : "))
c = num + 273.15  # Celsius to kelvin
f = (num * 9/5) + 32  # Celsius to Fahrenheit
print(f"Celsius {math.floor(c)}")
print(f"Fahrenheit {math.floor(f)}")