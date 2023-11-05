# Ввод размеров матрицы
n_D = int(input("Введите кол-во столбцов матрицы "))
m_D = int(input("Введите кол-во строк матрицы "))
if n_D > 0 and m_D > 0:
    # Инициализация матрицы
    D = [[] for _ in range(m_D)]
    # Заполнение матрицы
    for i in range(m_D):
        string = list(map(int, input("Введите очередную строчку матрицы: ").split()))
        if len(string) != n_D:
            print("Введена строчка, длина которой не соответствует длине строчки матрицы")
            break
        D[i] = string
    else:
        n_Z = int(input("Введите кол-во столбцов матрицы "))
        m_Z = int(input("Введите кол-во строк матрицы "))
        if 0 < n_Z <= m_Z and m_Z > 0:
            # Инициализация матрицы
            Z = [[] for _ in range(m_Z)]
            # Заполнение матрицы
            for i in range(m_Z):
                string = list(map(int, input("Введите очередную строчку матрицы: ").split()))
                if len(string) != n_Z:
                    print("Введена строчка, длина которой не соответствует длине строчки матрицы")
                    break
                Z[i] = string
            else:
                # Вывод матрицы
                print("Матрица D")
                for string in D:
                    for number in string:
                        print(f"{number:^10.7g}", end="")
                    print()
                # Вывод матрицы
                print("Матрица Z")
                for string in Z:
                    for number in string:
                        print(f"{number:^10.7g}", end="")
                    print()
                G = [0]*len(D)  # Инициализация списка G
                # Заполнение списка G
                for i in range(len(D)):
                    z_string_sum = sum(Z[i])
                    counter = 0
                    for elem in D[i]:
                        if elem > z_string_sum:
                            counter += 1
                    G[i] = counter
                maxG = max(G)
                # Вывод списка G и его максимума
                print("Список G", end=": ")
                for elem in G:
                    print(f"{elem:.5g}", end=" ")
                print()
                print(f"Максимальное значение в G: {maxG}")
                # Умножение матрицы на максимальное значение из списка
                for i in range(len(D)):
                    for j in range(len(D[i])):
                        D[i][j] = D[i][j] * maxG
                # Вывод умноженной матрицы
                print("Умноженная матрица D")
                for string in D:
                    for number in string:
                        print(f"{number:^10.7g}", end="")
                    print()
        else:
            print("Количество столбцов и количество строк матрицы должно быть больше нуля, а так же количество строк "
                  "матрицы Z должно быть больше или равно количеству строк матрицы D")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
