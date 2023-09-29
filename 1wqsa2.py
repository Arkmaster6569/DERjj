import math
def treugol(a, h):
    return 0.5 * a * h
def cvadrat(s):
    return s ** 2

def pramoygol(l, w):
    return l * w

def mnogo_ugol(s):
    return (3 * math.sqrt(3) * s ** 2) / 2

a = 6
h = 4
s1 = 6
l = 8
w = 20

t = treugol(a, h)
s2 = cvadrat(s1)
r = pramoygol(l, w)
h = mnogo_ugol(s2)

print("треугольника:", t)
print("квадрата:", s2)
print("прямоугольника:", r)
print("многоугольника:", h)
