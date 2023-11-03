# Неделин Никита ИУ7-16Б
# Переставить местами столбцы с максимальной и минимальной суммой элементов.


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
        # Инициализация переменных
        min_sum = sum([string[0] for string in matrix])
        min_sum_index = 0
        max_sum = sum([string[0] for string in matrix])
        max_sum_index = 0
        # Обновление переменных
        for i in range(1, n):
            current_sum = sum([string[i] for string in matrix])
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_index = i
            if current_sum < min_sum:
                min_sum = current_sum
                min_sum_index = i
        # Внесение изменений в матрицу
        for i in range(m):
            matrix[i][min_sum_index], matrix[i][max_sum_index] = matrix[i][max_sum_index], matrix[i][min_sum_index]
        # Вывод измененной матрицы
        print("Измененная матрица: ")
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
