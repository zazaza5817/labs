# Неделин Никита ИУ7-16Б
# Вариант 2
# Задание 2
# Ввод
n = int(input("Введите N - размер стороны матрицы: "))
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input("Введите строку матрицы (элементы деля пробелами): ").split()))


# Вывод введенной матрицы
print("Введенная матрица: ")
for string in matrix:
    for elem in string:
        print(f"{elem:8.5g}", end="")
    print()


# Перебор элементов которые лежат на или выше главной и побочной диагонали
# Перебор с 1 индекса т.к. в 1-нумерации это 2-й элемент, а перебрать необходимо только квадраты с четными номерами
for i in range(1, n//2, 2): 
    for j in range(i, n-i-1):
        # Сдвиг четырех элементов с временным хранением одного из них (по кругу)
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n-i-1]
        matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
        matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
        matrix[n-j-1][i] = temp


# Вывод преобразованной матрицы
print("Преобразованная матрица: ")
for string in matrix:
    for elem in string:
        print(f"{elem:8.5g}", end="")
    print()


# Запись в 0 элементы каждого столбца сумму всех элементов столбца для более удобного и немного более оптимального
# нахождения
for j in range(n):
    for i in range(1, n):
        matrix[0][j] += matrix[i][j]


# Инициализация переменных для поиска столбца по условию
max_count = 0
max_i = -1
# Поиск столбца по условию
for i in range(n):
    current_count = matrix[0].count(matrix[0][i])
    if current_count > max_count:
        max_i = i
        max_count = current_count


# Возвращение в нулевую ячейку найденного столбца исходного значения
for i in range(1, n):
    matrix[0][max_i] -= matrix[i][max_i]


# Вывод найденного столбца
print(f"Искомый столбец имеет индекс {max_i}")
for i in range(n):
    print(f"{matrix[i][max_i]:8.5g}")
