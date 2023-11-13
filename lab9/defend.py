# Неделин Никита ИУ7-16Б
N = int(input("Введите размер: "))


# Создание 3д матрицы
array_3d = [[[1 + (z + y * N + x * N ** 2) for z in range(N)] for y in range(N)] for x in range(N)]
if N > 0:
    print("Сгенерированная 3-д матрица:")
    for i in range(len(array_3d)):
        print(array_3d[i])
    # a = input("Введите по какому направлению выводить срез (X Y Z): ")
    index = int(input("Введите индекс среза: ")) - 1
    if 0 <= index < N:
        # Вывод нужного среза
        print("СРЕЗ по У")
        for x in range(N):
            for z in range(N):
                print(f"{array_3d[x][index][z]:10.7g}", end=" ")
            print()
        print("СРЕЗ по X")
        for y in range(N):
            for z in range(N):
                print(f"{array_3d[index][y][z]:10.7g}", end=" ")
            print()
        print("СРЕЗ по Z")
        for x in range(N):
            for y in range(N):
                print(f"{array_3d[x][y][index]:10.7g}", end=" ")
            print()
    else:
        print("Нет среза с таким индексом")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
