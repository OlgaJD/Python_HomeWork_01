# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


x1 = float(input('Введите координату первой точки по оси x: '))
y1 = float(input('Введите координату первой точки по оси y: '))
x2 = float(input('Введите координату второй точки по оси x: '))
y2 = float(input('Введите координату второй точки по оси y: '))

def distanse_in_2d (x1, y1, x2, y2):
    distanse = math.sqrt((x2-x1)**2+(y2-y1) **2)
    return distanse

print(f'Расстояние между точками равно {round(distanse_in_2d(x1, y1, x2, y2), 2)} ')