# Неделин Никита ИУ7-16Б
# Даны массивы D и F. Сформировать матрицу A по формуле
# aij = sin(di+fj).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.

from math import sin

# Ввод
lenD = int(input('Введите размера списка D: '))
lenF = int(input('Введите размера списка F: '))
if lenF > 0 and lenD > 0:
    D = [0.0] * lenD
    for i in range(lenD):
        D[i] = float(input(f'Введите {i + 1}-й элемент списка D: '))
    F = [0.0] * lenF
    for i in range(lenF):
        F[i] = float(input(f'Введите {i + 1}-й элемент списка F: '))

    # lenD - strings count
    # lenF - columns count
    # Инициализация матрицы и двух дополнительных столбцов
    matrix = [[0.0] * lenF for _ in range(lenD)]
    AV = [0.0] * lenD
    L = [0] * lenD

    # Генерация матрицы и дополнительных столбцов из заданных списков
    for i in range(lenD):
        positive_count = 0
        positive_sum = 0
        for j in range(lenF):  # Построчная генерация
            value = sin(D[i] + F[j])
            matrix[i][j] = value
            if value > 0:  # Обновление счетчиков при необходимости
                positive_count += 1
                positive_sum += value
        if positive_count > 0:  # Подсчет значений в дополнительных столбцах
            AV[i] = positive_sum / positive_count
            for j in range(lenF):
                if matrix[i][j] < AV[i]:
                    L[i] += 1
        else:
            AV[i] = -1
            L[i] = -1

    # вывод матрицы
    print(" " * 11 * lenF, end="")
    print(f"{'[AV]':<11s}{'[L]':<11s}")
    for i in range(len(matrix)):
        string = matrix[i]
        for elem in string:
            print(f"{elem:<11.5g}", end="")
        print(f"{AV[i]:<11.5g}{L[i]:<11.5g}")
else:
    print("Размеры обоих списков должны быть больше нуля")
