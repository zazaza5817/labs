# Импорт необходимых библиотек
import math
from typing import Callable


# Функция для вычисления приближенного значения интеграла методом правых прямоугольников
def right_rectangles(f, a, b, n):
    # Вычисление ширины каждого прямоугольника
    h = (b - a) / n
    # Инициализация результата
    result = 0
    # Суммирование значений функции в каждой точке
    for i in range(n):
        result += f(a + i * h)
    # Умножение результата на ширину прямоугольника
    result *= h
    # Возвращение результата
    return result


# Функция для вычисления приближенного значения интеграла методом трапеций
def trapezoids(f, a, b, n):
    # Вычисление ширины каждой трапеции
    h = (b - a) / n
    # Инициализация результата
    result = 0.5 * (f(a) + f(b))
    # Суммирование значений функции в каждой точке
    for i in range(1, n):
        result += f(a + i * h)
    # Умножение результата на ширину трапеции
    result *= h
    # Возвращение результата
    return result


# Функция для вычисления абсолютной и относительной погрешности
def error_calculation(f_integral, a, b, integral_value):
    # Вычисление истинного значения интеграла
    true_value = abs(f_integral(b) - f_integral(a))
    print(true_value)
    # Вычисление абсолютной погрешности
    absolute_error = abs(true_value - integral_value)
    # Вычисление относительной погрешности
    relative_error = absolute_error / abs(true_value) * 100
    # Возвращение абсолютной и относительной погрешности
    return absolute_error, relative_error


# Функция для вычисления оптимального количества разбиений для метода трапеций
def iterative_integration_trapezoids(func, a, b, eps):
    # Инициализация количества разбиений
    n = 1
    # Пока разница между результатами с разными количествами разбиений не достигнет заданной точности
    while n < 1000000:
        # Вычисление результатов для текущего и следующего количества разбиений
        i_n = trapezoids(func, a, b, n)
        i_2n = trapezoids(func, a, b, 2 * n)
        # Если разница между результатами меньше заданной точности, прерываем цикл
        if abs(i_n - i_2n) < eps:
            break
        # Удваиваем количество разбиений
        n *= 2
    else:
        # Возвращение ошибочного значение
        return -1
    # Возвращение оптимального количества разбиений
    return n


def is_number(s):
    s = s.strip()
    s = s.replace("_", "")
    if not s:
        return False
    # Проверка на целое число
    if is_signed_number(s):
        return True
    # Проверка на число с плавающей точкой
    elif '.' in s:
        parts = s.split('.')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            return False
        if not is_signed_number(parts[0]) or not parts[1].isdigit():
            return False
        return True
    # Проверка на число в экспоненциальной форме
    elif 'e' in s or 'E' in s:
        parts = s.split('e')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            return False
        if not is_signed_number(parts[0]) or not is_signed_number(parts[1]):
            return False
        return True
    # Если строка не прошла ни одну из проверок, она не является числом
    else:
        return False


# Проверка является ли строка целым числом
def is_signed_number(n):
    if n.isdigit():
        return True
    if n[0] == "-" and n[1:].isdigit():
        return True
    return False


# Функция для вычисления оптимального количества разбиений для метода правых прямоугольников
def iterative_integration_rectangles(func, a, b, eps):
    # Инициализация количества разбиений
    n = 1
    # Пока разница между результатами с разными количествами разбиений не достигнет заданной точности
    while n < 1000000:
        # Вычисление результатов для текущего и следующего количества разбиений
        i_n = right_rectangles(func, a, b, n)
        i_2n = right_rectangles(func, a, b, 2 * n)
        # Если разница между результатами меньше заданной точности, прерываем цикл
        if abs(i_n - i_2n) < eps:
            break
        # Удваиваем количество разбиений
        n *= 2
    # Возвращение оптимального количества разбиений
    else:
        return -1
    return n


# Главная функция программы
def main():
    # Ввод данных пользователем
    a = input("Введите начало отрезка интегрирования: ")
    if is_number(a):
        a = float(a)
    else:
        print("Введено не число")
        return 0
    b = input("Введите конец отрезка интегрирования: ")
    if is_number(b):
        b = float(b)
    else:
        print("Введено не число")
        return 0
    if a >= b:
        print("Заданного отрезка не существует")
        return 0
    n1 = input("Введите количество участков разбиения n1: ")
    if is_number(n1):
        if float(n1) == int(float(n1)):
            n1 = int(n1)
        else:
            print("Введено не целое число")
            return 0
    else:
        print("Введено не число")
        return 0

    n2 = input("Введите количество участков разбиения n2: ")
    if is_number(n2):
        if float(n2) == int(float(n2)):
            n2 = int(n2)
    else:
        print("Введено не число")
        return 0
    # Защита от ввода неверных значений n1 и n2
    if n1 <= 0 or n2 <= 0:
        print("n1 и n2 должны быть больше нуля")
        return 0
    # Функция интеграла и функция, которую интегрируем
    f_integral = math.cos
    f = math.sin
    # def f(x):
    #     return x ** 2
    #
    # def f_integral(x):
    #     return (x ** 3) / 3
    # Вычисление значений метода правых прямоугольников и метода трапеций для двух разных количеств разбиений
    value1_1 = right_rectangles(f, a, b, n1)
    value1_2 = trapezoids(f, a, b, n1)

    value2_1 = right_rectangles(f, a, b, n2)
    value2_2 = trapezoids(f, a, b, n2)

    # Вычисление абсолютной и относительной погрешности для каждого метода и каждого количества разбиений
    abs_error1_1, rel_error1_1 = error_calculation(f_integral, a, b, value1_1)
    abs_error1_2, rel_error1_2 = error_calculation(f_integral, a, b, value1_2)

    abs_error2_1, rel_error2_1 = error_calculation(f_integral, a, b, value2_1)
    abs_error2_2, rel_error2_2 = error_calculation(f_integral, a, b, value2_2)

    # Вывод таблицы с результатами
    print("-" * 64)
    print(f"|{'Метод':^20s}|{'n1':^20s}|{'n2':^20s}|")
    print(f"|{'':-^20s}|{'':-^20s}|{'':-^20s}|")
    print(f"|{'Правых треугольников':^20s}|{value1_1:^20.7g}|{value2_1:^20.7g}|")
    print(f"|{'':-^20s}|{'':-^20s}|{'':-^20s}|")
    print(f"|{'Трапеций':^20s}|{value1_2:^20.7g}|{value2_2:^20.7g}|")
    print("-" * 64)
    # Конец таблицы

    # Вывод абсолютной и относительной погрешности для каждого метода и каждого количества разбиений
    print(f"Абсолютная погрешность метода правых прямоугольников: {abs_error1_1:.6g}, {abs_error2_1:.6g}")
    print(f"Относительная погрешность метода правых прямоугольников (в %): {rel_error1_1:.6g}, {rel_error2_1:.6g}")
    print(f"Абсолютная погрешность метода трапеций (в %): {abs_error1_2:.6g}, {abs_error2_2:.6g}")
    print(f"Относительная погрешность метода трапеций: {rel_error1_2:.6g}, {rel_error2_2:.6g}")

    # Определение наиболее точного метода и вывод соответствующих результатов
    if min(abs_error1_1, abs_error1_2) < min(abs_error2_1, abs_error2_2):
        print("Метод правых прямоугольников является наиболее точным")
        eps = float(input("Введите точность epsilon для которой необходимо найти N: "))
        n = iterative_integration_trapezoids(f, a, b, eps)
        if n >= 0:
            print(f"Необходимое значение N для наименее точного метода: {n}")
        else:
            print("Не удалось достичь заданной точности при n < 1,000,000")
    elif min(abs_error1_1, abs_error1_2) > min(abs_error2_1, abs_error2_2):
        print("Метод трапеций является наиболее точным")
        eps = float(input("Введите точность epsilon для которой необходимо найти N: "))
        n = iterative_integration_rectangles(f, a, b, eps)
        if n >= 0:
            print(f"Необходимое значение N для наименее точного метода: {n}")
        else:
            print("Не удалось достичь заданной точности при n < 1,000,000")
    else:
        print("Оба метода имеют одинаковую точность")


if __name__ == "__main__":
    main()
