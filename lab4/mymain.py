from math import sin, log


#  definition of my functions
def a_generator(start, stop, step):
    while start <= stop:
        yield start
        start += step


def compare_by_eps(a, b):
    eps = 1e-2
    return abs(a - b) < eps


def h2(x):
    y = x * log(x) - 52
    return y


def h1(x):
    y = x / 2
    return y


a = 16
b = 20
step = 0.2

# Вывод шапки таблицы
print("-" * 46)
print(f'| {"a":^12} | {"h1":^12} | {"h2":^12} |')
print("-" * 46)

values_count = 0
for i in range(a * 10, int((b + step) * 10), int(step * 10)):
    print(f'| {i:^12.5g} | {h1(i):^12.5g} | {h2(i):^12.5g} |')
    values_count += 1
print("-" * 46)

# serif_count = int(input())  # input serif count
serif_count = 4

# Расчет значений на засечках графика
h2_values = list(map(h2, a_generator(a, b, step)))
graph_length = 120
delta = (max(h2_values) - min(h2_values)) / (serif_count - 1)
serif_values = []
for i in range(serif_count):
    serif_values.append(min(h2_values) + delta * i)

# Вывод шапки графика
title = "Построение графика"
print(values_count)
print(f"{title:=^{graph_length + 12}s}")
symbols_per_serif = round(graph_length / len(serif_values))
print(f"          |", end="")
for serif_value in serif_values:
    print(f"{serif_value:<{symbols_per_serif}.5g}", end="")
print("|")

# Подсчет коэффициента для вывода графика
try:
    scale_coefficient = (graph_length - 1) / (max(h2_values) - min(h2_values))
except:
    raise ValueError("Невозможно построить график, содержащий одну точку")

# Нахождение точки 0 на графике
space_position = round(0 - min(h2_values) * scale_coefficient) + 1


# Вывод графика
for x in range(a * 10, int((b + step) * 10), int(step * 10)):
    x = x / 10
    print(f"{x:<10.5g}|", end="")                                     # Вывод оси Х
    h2 = x * log(x) - 52
    normalized_value = h2 - min(h2_values)                            # Нормализация значения в точке х для вывода
    dot_position = round(normalized_value * scale_coefficient) + 1    # Положение точки относительно левого края графика
    spaces_after = (graph_length - dot_position)                      # Количество пробелов после точки графика
    if 0 < space_position < graph_length:                             # Проверка на пересечение графиком Ох
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

# while True:
#     print('ПУТИН КРУТОЙ!!!!!')
#     print('ЗЕЛЕНСКИЙ ЛОХ!!!')
