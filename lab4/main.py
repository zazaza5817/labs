# Неделин Никита ИУ7-16Б
# Программа для расчета таблицы значений функций и вывода графика одной из них
from math import log, sin  # Подключение библиотеки

a = float(input("Введите начальное значение: "))               # Число с которого следует перебирать иксы
b = float(input("Введите конечное значение: "))                # Число до которого следует перебирать иксы
step = float(input("Введите значение шага: "))                 # Шаг с которым следует перебирать иксы
# Коэффициент для вычисления дробных значений используя range()
if step < 1:
    range_coefficient = int(1/step)+1
else:
    range_coefficient = 1
graph_length = 3*20+32                # Длина графика
additional_if_const = 10              # Добавочное значение для графика если Y = const

# Вывод шапки таблицы
print("-" * 46)
print(f'| {"a":^12} | {"h1":^12} | {"h2":^12} |')
print("-" * 46)

# Вывод самой таблицы и подсчет минимума и максимума выводимой в график функции
min_value = float('+inf')
max_value = float('-inf')
for i in range(int(a * range_coefficient), int((b + step) * range_coefficient), int(step * range_coefficient)):
    i /= range_coefficient
    h1 = i**3 - 5.57*(i**2) - 193 * i - 633.1
    h2 = i * log(i) - 52
    max_value = max(max_value, h2)
    min_value = min(min_value, h2)
    print(f'| {i:^12.5g} | {h1:^12.5g} | {h2:^12.5g} |')
print("-" * 46)

# ввод кол-ва засечек
try:
    serif_count = int(input("Введите кол-во засечек: "))
except ValueError:
    raise ValueError("Кол-во засечек должно быть целым")
if not(4 <= serif_count <= 8):
    raise ValueError('Количество засечек должно быть от 4 до 8')


# Вывод шапки графика
if max_value == min_value:
    min_value = min_value - additional_if_const
    max_value = max_value + additional_if_const
delta = (max_value - min_value) / (serif_count - 1)
title = "Построение графика"
print(f"{title:=^{graph_length + 12}s}")  # +12 для отступа под ось х
# Вычисление кол-ва пробелов между засечками
spaces_between_serifs = round((graph_length - serif_count * 8) / (serif_count - 1))
print(f"          |", end="")
for i in range(serif_count):
    serif_value = min_value + delta * i
    if i < serif_count - 1:
        print(f"{serif_value:<8.5g}" + " " * spaces_between_serifs, end="")
    else:
        print(f"{serif_value:>8.5g}")

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
for x in range(int(a * range_coefficient), int((b + step) * range_coefficient), int(step * range_coefficient)):
    x = x / range_coefficient
    print(f"{x:<10.5g}|", end="")                                   # Вывод оси Х
    h2 = x * log(x) - 52                                            # Нахождение значения функции в точке х
    normalized_value = h2 - min_value                               # Нормализация значения в точке х для вывода
    dot_position = round(normalized_value * scale_coefficient) + 1  # Положение точки относительно левого края графика
    spaces_after = (graph_length - dot_position)                    # Количество пробелов после точки графика
    if 0 < space_position < graph_length:                           # Проверка на пересечение графиком Ох
        if space_position < dot_position:
            print(" " * (space_position - 1) + "|" + " " * (
                    dot_position - space_position - 1) + "*" + " " * spaces_after + "|")  # Вывод строчки
        elif space_position > dot_position:
            print(" " * (dot_position - 1) + "*" + " " * (space_position - dot_position - 1) + "|" + " " * (
                    spaces_after - (space_position - dot_position)) + "|")  # Вывод строчки
        else:
            print(" " * (dot_position - 1) + "*" + " " * spaces_after + "|")  # Вывод строчки
    else:
        print(" " * (dot_position - 1) + "*" + " " * spaces_after + "|")  # Вывод строчки без пересечения с Ох
