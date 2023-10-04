# Неделин Никита ИУ7-16Б
# Программа для расчета таблицы значений функций и вывода графика одной из них
from math import log  # Подключение библиотеки

a = 16                     # Число с которого следует перебирать иксы
b = 20                     # Число до которого следует перебирать иксы
step = 0.1                 # Шаг с которым следует перебирать иксы
range_coefficient = 10     # Коэффициент для вычисления дробных значений используя range()
graph_length = 120         # Длина графика

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
    # h2 = 1
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

# Расчет значений на засечках графика
delta = (max_value - min_value) / (serif_count - 1)
serif_values = []
for i in range(serif_count):
    serif_values.append(min_value + delta * i)

# Вывод шапки графика
title = "Построение графика"
print(f"{title:=^{graph_length + 12}s}")
symbols_per_serif = round(graph_length / len(serif_values))
print(f"          |", end="")
for serif_value in serif_values:
    print(f"{serif_value:<{symbols_per_serif}.5g}", end="")
print("|")

# Подсчет коэффициента для вывода графика
try:
    scale_coefficient = (graph_length - 1) / (max_value - min_value)
    # print(scale_coefficient)
except ZeroDivisionError:
    scale_coefficient = (graph_length - 1) / (max_value / 2)

# Нахождение y = 0 на графике
space_position = round(0 - min_value * scale_coefficient) + 1

# Вывод графика
for x in range(int(a * range_coefficient), int((b + step) * range_coefficient), int(step * range_coefficient)):
    x = x / 10
    print(f"{x:<10.5g}|", end="")  # Вывод оси Х
    h2 = x * log(x) - 52  # Нахождение значения функции в точке х
    normalized_value = h2 - min_value  # Нормализация значения в точке х для вывода
    dot_position = round(normalized_value * scale_coefficient) + 1  # Положение точки относительно левого края графика
    spaces_after = (graph_length - dot_position)  # Количество пробелов после точки графика
    if 0 < space_position < graph_length:  # Проверка на пересечение графиком Ох
        if space_position < dot_position:
            print(" " * (space_position - 1) + "|" + " " * (
                    dot_position - space_position - 1) + "*" + " " * spaces_after + "|")
        elif space_position > dot_position:
            print(" " * (dot_position - 1) + "*" + " " * (space_position - dot_position - 1) + "|" + " " * (
                    spaces_after - (space_position - dot_position)) + "|")
        else:
            print(" " * (dot_position - 1) + "*" + " " * spaces_after + "|")
    else:
        print(" " * (dot_position - 1) + "*" + " " * spaces_after + "|")  # Вывод строчки без пересечения с Ох
