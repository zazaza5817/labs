# Правых прямоугольников
# Трапеций
import math
from typing import Callable


# Функция для вычисления приближенного значения интеграла методом правых прямоугольников
def right_rectangles(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * h)
    result *= h
    return result


# Функция для вычисления приближенного значения интеграла методом трапеций
def trapezoids(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """Вычисление приближенного значения интеграла методом трапеций"""
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def error_calculation(f_integral, a, b, integral_value):
    true_value = f_integral(b) - f_integral(a)
    absolute_error = abs(true_value - integral_value)
    relative_error = absolute_error / abs(true_value)
    return absolute_error, relative_error


def iterative_integration_trapezoids(func, a, b, eps):
    n = 1
    while True:
        i_n = trapezoids(func, a, b, n)
        i_2n = trapezoids(func, a, b, 2 * n)
        if abs(i_n - i_2n) < eps:
            break
        n *= 2
    return n


def iterative_integration_rectangles(func, a, b, eps):
    n = 1
    while True:
        i_n = right_rectangles(func, a, b, n)
        i_2n = right_rectangles(func, a, b, 2 * n)
        if abs(i_n - i_2n) < eps:
            break
        n *= 2
    return n


def main():
    a = float(input("Введите начало отрезка интегрирования: "))
    b = float(input("Введите конец отрезка интегрирования: "))
    n1 = int(input("Введите количество участков разбиения n1: "))
    n2 = int(input("Введите количество участков разбиения n2: "))

    f_integral = math.cos
    f = math.sin

    value1_1 = right_rectangles(f, a, b, n1)
    value1_2 = trapezoids(f, a, b, n1)

    value2_1 = right_rectangles(f, a, b, n2)
    value2_2 = trapezoids(f, a, b, n2)

    abs_error1_1, rel_error1_1 = error_calculation(f_integral, a, b, value1_1)
    abs_error1_2, rel_error1_2 = error_calculation(f_integral, a, b, value1_2)

    abs_error2_1, rel_error2_1 = error_calculation(f_integral, a, b, value2_1)
    abs_error2_2, rel_error2_2 = error_calculation(f_integral, a, b, value2_2)

    # Таблица
    print("-" * 64)
    print(f"|{'Метод':^20s}|{'n1':^20s}|{'n2':^20s}|")
    print(f"|{'':-^20s}|{'':-^20s}|{'':-^20s}|")
    print(f"|{'Правых треугольников':^20s}|{value1_1:^20.7g}|{value2_1:^20.7g}|")
    print(f"|{'':-^20s}|{'':-^20s}|{'':-^20s}|")
    print(f"|{'Трапеций':^20s}|{value1_2:^20.7g}|{value2_2:^20.7g}|")
    print("-" * 64)
    # Конец таблицы
    print(
        f"Абсолютная погрешность метода правых прямоугольников: {format(abs_error1_1, '.6f')}, {format(abs_error2_1, '.6f')}")
    print(
        f"Относительная погрешность метода правых прямоугольников: {format(rel_error1_1, '.6f')}, {format(rel_error2_1, '.6f')}")
    print(f"Абсолютная погрешность метода трапеций: {format(abs_error1_2, '.6f')}, {format(abs_error2_2, '.6f')}")
    print(f"Относительная погрешность метода трапеций: {format(rel_error1_2, '.6f')}, {format(rel_error2_2, '.6f')}")

    if min(abs_error1_1, abs_error1_2) < min(abs_error2_1, abs_error2_2):
        print("Метод правых прямоугольников является наиболее точным")
        eps = float(input("Введите точность epsilon для которой необходимо найти N: "))
        print(f"Необходимое значение N для наименее точного метода: {iterative_integration_trapezoids(f, a, b, eps)}")
    elif min(abs_error1_1, abs_error1_2) > min(abs_error2_1, abs_error2_2):
        print("Метод трапеций является наиболее точным")
        eps = float(input("Введите точность epsilon для которой необходимо найти N: "))
        print(f"Необходимое значение N для наименее точного метода: {iterative_integration_rectangles(f, a, b, eps)}")
    else:
        print("Оба метода имеют одинаковую точность")


if __name__ == "__main__":
    main()
