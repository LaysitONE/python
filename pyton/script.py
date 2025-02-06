import math

x = float(input("Введите значение x: \n"))
z = float(input("Введите значение z: \n"))
a = float(input("Введите значение a: \n"))

num1 = x ** 3 + z
dtrm1 = x + 1
term1 = num1 / dtrm1

term2 = abs(x - a**5)

num2 = x ** (2 / 3) + z * x
dtrm2 = 3 - z ** 4
term3 = num2 / dtrm2

b = term1 - term2 + term3

print(f"Значение b: {b}")