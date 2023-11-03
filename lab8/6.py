# Неделин Никита ИУ7-16Б
# Транспонирование квадратной матрицы


# Ввод размера матрицы
n = int(input("Введите размер квадратной матрицы: "))
if n > 0:
    matrix = [[] for _ in range(n)]
    for i in range(n):
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
        # Транспонирование матрицы
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Вывод матрицы
        print("Измененная матрица: ")
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
