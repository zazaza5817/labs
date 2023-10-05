# Неделин Никита ИУ7-16Б
# Программа для расчета таблицы значений функций и вывода графика одной из них
from math import log  # Подключение библиотеки

a = float(input("Введите начальное значение: "))       # Число с которого следует перебирать иксы
b = float(input("Введите конечное значение: "))        # Число до которого следует перебирать иксы
step = float(input("Введите значение шага: "))         # Шаг с которым следует перебирать иксы
range_coefficient = 100000                               # Коэффициент для вычисления дробных значений используя range()
graph_length = 3*35+32                                   # Длина графика
additional_if_const = 10                                 # Добавочное значение для графика если Y = const


# Вывод шапки таблицы
print("-" * 61)
print(f'| {"r":^12} | {"q1":^12} | {"q2":^12} | {"q3":^12} |')
print("-" * 61)

# Вывод самой таблицы и подсчет минимума и максимума выводимой в график функции
min_value = float('+inf')
max_value = float('-inf')
dop_summ = 0
for r in range(int(a * range_coefficient), int((b + step) * range_coefficient), int(step * range_coefficient)):
    r /= range_coefficient
    q1 = r ** 3 - 5.57 * (r ** 2) - 193 * r - 633.1
    q2 = r * log(r) - 52
    q3 = (q1 ** 3 - q2 ** 3) / 1000
    if q2 > 0:
        dop_summ += q2
    max_value = max(max_value, q3)
    min_value = min(min_value, q3)
    print(f'| {r:^12.5g} | {q1:^12.5g} | {q2:^12.5g} | {q3:^12.5g} |')
print("-" * 61)

# ввод кол-ва засечек
try:
    serif_count = int(input("Введите кол-во засечек: "))
except ValueError:
    raise ValueError("Кол-во засечек должно быть целым")
if not(4 <= serif_count <= 8):
    raise ValueError('Количество засечек должно быть от 4 до 8')


# Вывод шапки графика
symbols_per_sherif = 10
if max_value == min_value:
    min_value = min_value - additional_if_const
    max_value = max_value + additional_if_const
delta = (max_value - min_value) / (serif_count - 1)
title = "Построение графика"
print(f"{title:=^{graph_length + 12}s}")  # +12 для отступа под ось х
# Вычисление кол-ва пробелов между засечками
spaces_between_serifs = round((graph_length - serif_count * symbols_per_sherif) / (serif_count - 1))
print(f"          |", end="")
for i in range(serif_count):
    serif_value = min_value + delta * i
    if i < serif_count - 1:
        print(f"{serif_value:<{symbols_per_sherif}.4g}" + " " * spaces_between_serifs, end="")
    else:
        print(f"{serif_value:>{symbols_per_sherif}.4g}")

# Подсчет коэффициента для вывода графика
try:
    scale_coefficient = (graph_length - 1) / (max_value - min_value)
except ZeroDivisionError:
    # Выполняется если Y не меняется на заданном диапазоне X, или если его изменения в пределах погрешности
    min_value = min_value - additional_if_const
    max_value = max_value + additional_if_const
    scale_coefficient = (graph_length - 1) / (max_value - min_value)

# Нахождение y = 0 на графике
space_position = round(0 - min_value * scale_coefficient) + 1

# Вывод графика
for r in range(int(a * range_coefficient), int((b + step) * range_coefficient), int(step * range_coefficient)):
    r = r / range_coefficient
    print(f"{r:^10.5g}|", end="")                                   # Вывод оси Х
    q1 = r ** 3 - 5.57 * (r ** 2) - 193 * r - 633.1
    q2 = r * log(r) - 52                                            # Нахождение значения функции в точке х
    q3 = (q1 ** 3 - q2 ** 3) / 1000
    normalized_value = q3 - min_value                               # Нормализация значения в точке х для вывода
    dot_position = round(normalized_value * scale_coefficient) + 1  # Положение точки относительно левого края графика
    spaces_after = (graph_length - dot_position)                    # Количество пробелов после точки графика
    if 0 < space_position < graph_length:                           # Проверка на пересечение графиком Ох
        if space_position < dot_position:
            print(" " * (space_position - 1) + "|" + " " * (dot_position - space_position - 1) +
                  "*" + " " * spaces_after + "|")  # Вывод строчки
        elif space_position > dot_position:
            print(" " * (dot_position - 1) + "*" + " " * (space_position - dot_position - 1) + "|" +
                  " " * (spaces_after - (space_position - dot_position)) + "|")  # Вывод строчки
        else:
            print(" " * (dot_position - 1) + "*" + " " * spaces_after + "|")  # Вывод строчки
    else:
        print(" " * (dot_position - 1) + "*" + " " * spaces_after + "|")  # Вывод строчки без пересечения с Ох
print(f"Дополнительное задание. Искомая сумма: {dop_summ:.5g}")  # Вывод дополнительного задания
