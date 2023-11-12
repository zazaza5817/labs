# Неделин Никита ИУ7-16Б

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
        print("Исходная матрица")
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
        # Поворот на 90 по часовой стрелке квадратом
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
        # Вывод матрицы
        print("Промежуточная матрица")
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
        # Поворот на 90 против часовой стрелке квадратом
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = tmp
        # Вывод матрицы
        print("Итоговая матрица матрица")
        for string in matrix:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
