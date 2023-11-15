# Правых прямоугольников
# Трапеций
import math


# Функция для вычисления приближенного значения интеграла методом правых прямоугольников
def right_rectangles(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * h)
    result *= h
    return result


# Функция для вычисления приближенного значения интеграла методом трапеций
def trapezoids(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def error_calculation(f_integral, f, a, b, n, method):
    integral_value = method(f, a, b, n)
    true_value = f_integral(b) - f_integral(a)
    absolute_error = abs(true_value - integral_value)
    relative_error = absolute_error / abs(true_value)
    return absolute_error, relative_error


def main():
    a = float(input("Введите начало отрезка интегрирования: "))
    b = float(input("Введите конец отрезка интегрирования: "))
    n1 = int(input("Введите количество участков разбиения для первого измерения метода правых прямоугольников: "))
    n2 = int(input("Введите количество участков разбиения для первого измерения метода трапеций: "))

    f_integral = math.cos
    f = math.sin

    abs_error1_1, rel_error1_1 = error_calculation(f_integral, f, a, b, n1, right_rectangles)
    abs_error1_2, rel_error1_2 = error_calculation(f_integral, f, a, b, n1, trapezoids)

    abs_error2_1, rel_error2_1 = error_calculation(f_integral, f, a, b, n2, right_rectangles)
    abs_error2_2, rel_error2_2 = error_calculation(f_integral, f, a, b, n2, trapezoids)

    value1_1 = right_rectangles(f, a, b, n1)
    value1_2 = trapezoids(f, a, b, n1)

    value2_1 = right_rectangles(f, a, b, n2)
    value2_2 = trapezoids(f, a, b, n2)
    # Тут таблица
    print(f"Значения метода правых прямоугольников: {format(value1_1, '.6f')}, {format(value2_1, '.6f')}")
    print(f"Значения метода трапеций: {format(value1_2, '.6f')}, {format(value2_2, '.6f')}")
    # Конец таблицы
    print(f"Абсолютная погрешность метода правых прямоугольников: {format(abs_error1_1, '.6f')}, {format(abs_error2_1, '.6f')}")
    print(f"Относительная погрешность метода правых прямоугольников: {format(rel_error1_1, '.6f')}, {format(rel_error2_1, '.6f')}")
    print(f"Абсолютная погрешность метода трапеций: {format(abs_error1_2, '.6f')}, {format(abs_error2_2, '.6f')}")
    print(f"Относительная погрешность метода трапеций: {format(rel_error1_2, '.6f')}, {format(rel_error2_2, '.6f')}")

    if min(abs_error1_1, abs_error1_2) < min(abs_error2_1, abs_error2_2):
        print("Метод правых прямоугольников является наиболее точным")
    elif min(abs_error1_1, abs_error1_2) > min(abs_error2_1, abs_error2_2):
        print("Метод трапеций является наиболее точным")
    else:
        print("Оба метода имеют одинаковую точность")


if __name__ == "__main__":
    main()
