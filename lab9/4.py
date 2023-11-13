# Неделин Никита ИУ7-16Б
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
        # Ввод списка строк в которых необходимо найти максимум
        prompt = "Введите номера строчек в которых необходимо найти максимальные значения через пробел: "
        string_numbers = list(map(int, input(prompt).split()))
        max_elms = []
        # Нахождение максимумов по заданным строчкам
        for i in string_numbers:
            if i < 0 or i >= len(matrix):
                print(f"В матрице нет строчки с номером {i}")
                break
            max_elms.append(max(matrix[i]))
        else:
            # Вывод заданного списка и найденных значений
            print("Номера строчек, в которых необходимо найти максимальные значения: ")
            for elem in string_numbers:
                print(f"{elem:.7g}", end=" ")
            print("\nМаксимальные значения: ")
            for elem in max_elms:
                print(f"{elem:.7g}", end=" ")
            print()
            if len(max_elms) != 0:
                avg = sum(max_elms)/len(max_elms)
                print(f"Среднее арифметическое максимальных значений: {avg:.5g}")
            else:
                print("Невозможно посчитать среднее арифметическое (нет значений)")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
