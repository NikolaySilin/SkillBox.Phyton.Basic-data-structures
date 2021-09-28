# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

square = 3.1415926 * radius ** 2
square_4 = (round(square, 4))
square_4 = str(square_4)
print('Square of a circle = ' + square_4)

# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

center = (0, 0)

center_point_distance = ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) ** 0.5
center_point_distance = str(center_point_distance)
point_in_a_circle = ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) < radius ** 2
point_in_a_circle = str(point_in_a_circle)
print('Distance from point to center = ' + center_point_distance)
print("Point in a circle = " + point_in_a_circle)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

center_point_2_distance = ((point_2[0] - center[0]) ** 2 + (point_2[1] - center[1]) ** 2) ** 0.5
center_point_2_distance = str(center_point_2_distance)
point_2_in_a_circle = ((point_2[0] - center[0]) ** 2 + (point_2[1] - center[1]) ** 2) < radius ** 2
point_2_in_a_circle = str(point_2_in_a_circle)
print('\nDistance from point_2 to center = ' + center_point_2_distance)
print("Point_2 in a circle = " + point_2_in_a_circle)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False
