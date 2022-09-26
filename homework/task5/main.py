import math
print("Введите координаты точки А:")
x_A = float(input("Координата X:"))
y_A = float(input("Координата Y:"))
print("Введите координаты точки B:")
x_B = float(input("Координата X:"))
y_B = float(input("Координата Y:"))
sqrt = round(math.sqrt((x_A - x_B) ** 2 + (y_A - y_B) ** 2), 3)
print('Расстояние между точками =', sqrt)