a = float(input("Введите a = "))
b = float(input("Введите b = "))
c = float(input("Введите c = "))
d = float(input("Введите d = "))

s = a * b * c * d

print(s)

import math

r = float(input("Введите радиус круга: "))

c = math.pi * (r ** 2)

print(c)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

s = (a + b + c) / 2

t = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(t)
