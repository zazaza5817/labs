# Вариант 5
# Неделин Никита ИУ7-16Б
# Нахождение строки в матрице с наибольшим числом нулевых элементов


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
        # Инициализация переменных максимального количества нулей и индекса строки с этим количеством нулей
        max_zero_count = matrix[0].count(0)
        max_string_index = 0
        # Нахождение строки с максимальным количеством нулей
        for i in range(1, m):
            zero_count = matrix[i].count(0)
            if zero_count > max_zero_count:
                max_zero_count = zero_count
                max_string_index = i
        # Вывод
        print("Найденная строка: ")
        for number in matrix[max_string_index]:
            print(f"{number:^10.7g}", end="")
        print(f"[{max_string_index:^.7g}]")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
