# Неделин Никита ИУ7-16Б
X = int(input("Введите размер X: "))
Y = int(input("Введите размер Y: "))
Z = int(input("Введите размер Z: "))

# Создание 3д матрицы
array_3d = [[[0 for z in range(Z)] for y in range(Y)] for x in range(X)]
if X > 0 and Y > 0 and Z > 0:
    flag = True
    for x in range(X):
        if not flag:
            break
        print(f"X = {x+1}")
        matrix_slice = [[0 for _ in range(Z)] for _ in range(Y)]
        for y in range(Y):
            if not flag:
                break
            string = list(map(int, input(f"Введите строчку при Y = {y+1}: ").split()))
            if len(string) != Z:
                print("Количество элементов в строчке не соответствует заданному Z")
                flag = False
                break
            matrix_slice[y] = string
        if not flag:
            break
        array_3d[x] = matrix_slice
    else:
        index = int(input("Введите индекс среза: ")) - 1
        if 0 <= index < Y:
            # Вывод нужного среза
            for x in range(X-1, -1, -1):
                for z in range(Z):
                    print(f"{array_3d[x][index][z]:10.7g}", end=" ")
                print()
        else:
            print("Нет среза с таким индексом")
