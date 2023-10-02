# Подключение библиотеки
from math import sqrt, isclose


# Объявление функции для подсчета расстояния от точки до прямой в координатах
def calc_distance(xa, ya, xb, yb, mx, my):
    ab = (xb - xa, yb - ya)  # Нахождение координат вектора AB
    am = (mx - xa, my - ya)  # Нахождение координат вектора AM
    # Нахождение длин векторов
    ab_length = sqrt(ab[0] ** 2 + ab[1] ** 2)
    am_length = sqrt(am[0] ** 2 + am[1] ** 2)
    # Нахождение синуса между векторами
    cos = ((ab[0] * am[0] + ab[1] * am[1]) / (ab_length * am_length))
    sin = sqrt(1 - cos ** 2)
    # Нахождение площади параллелограмма, построенного на векторах
    square = ab_length * am_length * sin
    # Нахождение высоты параллелограмма = расстояния от точки до прямой
    distance = square / ab_length
    return distance


# def isclose(a, b):
#     eps = 1e-7
#     if abs(a - b) < eps:
#         return True
#     return False


def square(x1, y1, x2, y2, x3, y3):
    triangle_sides = [sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2),
                      sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)]
    p = sum(triangle_sides)/2
    return sqrt(p*(p-triangle_sides[0])*(p-triangle_sides[1])*(p-triangle_sides[2]))


# Ввод координат точек вершин
try:
    x1, y1 = map(int, input("Введите координаты первой точки через пробел: ").split())
    x2, y2 = map(int, input("Введите координаты второй точки через пробел: ").split())
    x3, y3 = map(int, input("Введите координаты третьей точки через пробел: ").split())
except:
    raise ValueError("Неверный формат координат точки")
if isclose(square(x1, y1, x2, y2, x3, y3), 0):
    raise ValueError("Заданные точки не образовывают треугольник")
# Вычисление длин сторон треугольника
sides = [sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2),
         sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)]
sides.sort()


ma = sqrt((2 * sides[1] ** 2 + 2 * sides[2] ** 2 - sides[0] ** 2) / 4)  # Вычисление медианы из меньшего угла
p = sum(sides)  # Вычисление периметра

print("Сумма длин сторон треугольника: %g" % p)  # Вывод
print("Длина медианы, проведенной из минимального угла: %g" % ma)  # Вывод
# Вывод

if ((sides[0] ** 2 + sides[1] ** 2) < sides[2] ** 2) and not isclose((sides[0] ** 2 + sides[1] ** 2), sides[2] ** 2):
    print("Треугольник тупоугольный")
else:
    print("Треугольник не тупоугольный")


try:
    x0, y0 = map(int, input("Введите координаты точки через пробел: ").split())  # Ввод координат точки
except:
    raise ValueError("Неверный формат координат точки")
# проекция на ось Z вектора, полученного путём векторного произведения вектора стороны треугольника и вектора из
# точки до начала этой стороны
pr1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
pr2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
pr3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
if not (isclose(pr1, 0) or isclose(pr2, 0) or isclose(pr3, 0)):
    if (pr1 > 0) == (pr2 > 0) == (pr3 > 0):
        print("Точка расположена внутри треугольника")
        min_distance = min(calc_distance(x1, y1, x2, y2, x0, y0), calc_distance(x1, y1, x3, y3, x0, y0),
                           calc_distance(x2, y2, x3, y3, x0, y0))
        print("Минимальное расстояние от точки до стороны треугольника или ее продолжения: %g" % min_distance)
    else:
        print("Точка расположена вне треугольника")

else:
    print("Точка расположена на стороне треугольника")
