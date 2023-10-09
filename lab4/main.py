# Неделин Никита ИУ7-16Б
# Программа для расчета таблицы значений функций и вывода графика одной из них
from math import log, isclose  # Подключение библиотеки

a = float(input("Введите начальное значение: "))       # Число с которого следует перебирать иксы
b = float(input("Введите конечное значение: "))        # Число до которого следует перебирать иксы
step = float(input("Введите значение шага: "))         # Шаг с которым следует перебирать иксы
range_coefficient = 1e5                                # Коэффициент для вычисления дробных значений используя range()
graph_length = 3*35+32                                 # Длина графика
additional_if_const = 10                               # Добавочное значение для графика если Y = const


if not isclose(step, 0):
    has_dots = False
    for r in range(int(a * range_coefficient), int(b * range_coefficient) + 1, int(step * range_coefficient)):
        has_dots = True
        break
    if has_dots:
        # Вывод шапки таблицы
        print("-" * 61)
        print(f'| {"r":^12} | {"q1":^12} | {"q2":^12} | {"q3":^12} |')
        print("-" * 61)
        # Вывод самой таблицы и подсчет минимума и максимума выводимой в график функции
        min_value = float('+inf')
        max_value = float('-inf')
        # graph_start_value = float('-inf')
        dop_summ = 0
        points_counter = 0
        flag = False
        for r in range(int(a * range_coefficient), int(b * range_coefficient) + 1, int(step * range_coefficient)):
            r /= range_coefficient
            q1 = r ** 3 - 5.57 * (r ** 2) - 193 * r - 633.1
            if r > 0:
                if points_counter == 0:
                    a = r
                points_counter += 1
                q2 = r * log(r) - 52
                q3 = (q1 ** 3 - q2 ** 3) / 1000
                if q2 > 0:
                    dop_summ += q2

                max_value = max(max_value, q3)
                min_value = min(min_value, q3)
                print(f'| {r:^12.5g} | {q1:^12.5g} | {q2:^12.5g} | {q3:^12.5g} |')
            else:
                if points_counter != 0 and not flag:
                    b = r - step
                    flag = True
                print(f'| {r:^12.5g} | {q1:^12.5g} | {"--":^12s} | {"--":^12s} |')
        print("-" * 61)

        if points_counter > 0:
            # ввод кол-ва засечек
            while True:
                serif_count = int(input("Введите кол-во засечек: "))
                if not(4 <= serif_count <= 8):
                    print('Количество засечек должно быть от 4 до 8')
                else:
                    break
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
                    print(f"{serif_value:<{symbols_per_sherif}.5g}" + " " * spaces_between_serifs, end="")
                else:
                    print(f"{serif_value:>{symbols_per_sherif}.5g}")

            # Подсчет коэффициента для вывода графика
            if not isclose(max_value, min_value):
                scale_coefficient = (graph_length - 1) / (max_value - min_value)
            else:
                # Выполняется если Y не меняется на заданном диапазоне X, или если его изменения в пределах погрешности
                min_value = min_value - additional_if_const
                max_value = max_value + additional_if_const
                scale_coefficient = (graph_length - 1) / (max_value - min_value)

            mean_value = a + ((points_counter//2) * step)
            q1 = mean_value ** 3 - 5.57 * (mean_value ** 2) - 193 * mean_value - 633.1
            q2 = mean_value * log(mean_value) - 52
            mean_y = (q1 ** 3 - q2 ** 3) / 1000
            # Нахождение y = 0 на графике
            line_position = round((mean_y - min_value) * scale_coefficient) + 1

            # Вывод графика
            for r in range(int(a * range_coefficient), int(b * range_coefficient) + 1, int(step * range_coefficient)):
                r = r / range_coefficient
                print(f"{r:^10.5g}|", end="")                                   # Вывод оси Х
                q1 = r ** 3 - 5.57 * (r ** 2) - 193 * r - 633.1
                q2 = r * log(r) - 52                                            # Нахождение значения функции в точке х
                q3 = (q1 ** 3 - q2 ** 3) / 1000
                normalized_value = q3 - min_value                          # Нормализация значения в точке х для вывода
                dot_position = round(normalized_value * scale_coefficient) + 1  # Положение точки с левого края графика
                spaces_after = (graph_length - dot_position)                 # Количество пробелов после точки графика
                spacer = " "
                if isclose(r, mean_value):
                    spacer = "-"
                if 0 < line_position < graph_length:                           # Проверка на пересечение графиком Ох
                    if line_position < dot_position:
                        print(spacer * (line_position - 1) + "|" + spacer * (dot_position - line_position - 1) +
                              "*" + spacer * spaces_after + "|")  # Вывод строчки
                    elif line_position > dot_position:
                        print(spacer * (dot_position - 1) + "*" + spacer * (line_position - dot_position - 1) + "|" +
                              spacer * (spaces_after - (line_position - dot_position)) + "|")  # Вывод строчки
                    else:
                        print(spacer * (dot_position - 1) + "*" + spacer * spaces_after + "|")  # Вывод строчки
                else:
                    print(spacer * (dot_position - 1) + "*" + spacer * spaces_after + "|")  # Вывод строчки без пересечения с Ох
        print(f"Дополнительное задание. Искомая сумма: {dop_summ:.5g}")  # Вывод дополнительного задания
    else:
        print("Диапазон не имеет ни одной точки")
else:
    print("Шаг не может быть равен 0")
