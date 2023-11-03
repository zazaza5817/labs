# Неделин Никита ИУ7-16Б
# Найти максимальное значение в квадратной матрице над главной диагональю и минимальное - под побочной диагональю.


# Ввод размера матрицы
n = int(input("Введите размер квадратной матрицы: "))
if n > 0:
    if n != 1:
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
            # Нахождение максимального значения над главной диагональю
            max_value = float('-inf')
            for i in range(n):
                for j in range(i+1, n):
                    max_value = max(max_value, matrix[i][j])
            # Нахождение минимального значения под побочной диагональю
            min_value = float('+inf')
            for i in range(1, n):
                for j in range(n-i, n):
                    min_value = min(min_value, matrix[i][j])
            print(f"Максимальное значение над главной диагональю: {max_value:<9.6g}")
            print(f"Минимальное значение под побочной диагональю: {min_value:<9.6g}")
    else:
        print("В матрице 1x1 нет элементов над главной и под побочной диагональю")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
