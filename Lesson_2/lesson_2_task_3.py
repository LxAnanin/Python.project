import math

print("Введите сторону квадрата: ", end='')
sideSqr = float(input())

def square(side):
    sideRound = math.ceil(side)
    sqr = sideRound*sideRound
    print("Площадь квадрата равна:", sqr)

square(sideSqr)