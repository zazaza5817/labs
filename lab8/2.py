# Неделин Никита ИУ7-16Б
# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.


# объявление функции для подсчета отрицательных элементов в списки
def count_negatives(lst):
    counter = 0
    for elem in lst:
        if elem < 0:
            counter += 1
    return counter


# Ввод размеров матрицы
n = int(input("Введите кол-во столбцов матрицы "))
m = int(input("Введите кол-во строк матрицы "))
if n > 0 and m > 0:
    # Инициализация матрицы
    matrix = [[] for _ in range(m)]
    # Заполнение матрицы
    for i in range(m):
        string = list(map(int, input("Введите очередную строчку матрицы: ").split()))
        if len(string) != n:
            print("Введена строчка, длина которой не соответствует длине строчки матрицы")
            break
        matrix[i] = string
    else:
        # Вывод матрицы
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
        # Инициализация переменных для обработки матрицы
        min_negatives_count = count_negatives(matrix[0])
        max_negatives_count = count_negatives(matrix[0])
        min_negatives_index = 0
        max_negatives_index = 0
        # Обновление переменных для обработки матрицы
        for i in range(1, m):
            current_negatives_count = count_negatives(matrix[i])
            if current_negatives_count < min_negatives_count:
                min_negatives_count = current_negatives_count
                min_negatives_index = i
            if current_negatives_count > max_negatives_count:
                max_negatives_count = current_negatives_count
                max_negatives_index = i
        # Обработка матрицы
        matrix[max_negatives_index], matrix[min_negatives_index] = (
            matrix[min_negatives_index], matrix[max_negatives_index])
        # Вывод измененной матрицы
        print("Измененная матрица: ")
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
