n = int(input("Введите кол-во столбцов матрицы "))
m = int(input("Введите кол-во строк матрицы "))
if n > 0 and m > 0:
    # Инициализация матрицы
    A = [[] for _ in range(m)]
    B = [[] for _ in range(m)]
    for i in range(2*m):
        string = list(map(int, input(f"Введите очередную строчку матрицы {(i//m)+1}: ").split()))
        if len(string) != n:
            print("Введена строчка, длина которой не соответствует длине строчки матрицы")
            break
        if i//m == 0:
            A[i] = string
        else:
            B[i-m] = string
    else:
        # Вывод матрицы А
        print("Введенная матрица A:")
        for string in A:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
        # Вывод матрицы В
        print("Введенная матрица B:")
        for string in B:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
        # Создание пустой матрицы С
        C = [[0 for _ in range(n)] for _ in range(m)]
        # Перемножение матриц А и В
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] * B[i][j]
        # Вывод матрицы C
        print("Сформированная матрица C:")
        for string in C:
            for number in string:
                print(f"{number:^10.7g}", end="")
            print()
        # Нахождение значений V
        V = [0 for _ in range(n)]
        for i in range(len(A)):
            for j in range(n):
                V[j] += C[i][j]
        # Вывод V
        print("Значения V:")
        for number in V:
            print(f"{number:.7g}", end=" ")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
