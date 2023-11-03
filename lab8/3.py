# Вариант 5
# Неделин Никита ИУ7-16Б
# Найти столбец, имеющий наибольшее кол-во чисел, являющихся степенью 2


# Объявление функции для подсчета чисел равных степени двойки в списке
def count_powers(lst):
    counter = 0
    for elem in lst:
        while elem % 2 == 0 and elem > 1:
            elem //= 2
        if elem == 1:
            counter += 1
    return counter


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
        max_count_powers = count_powers([string[0] for string in matrix])
        max_powers_index = 0
        # Обновление переменных
        for i in range(1, n):
            current_count_powers = count_powers([string[i] for string in matrix])
            if current_count_powers > max_count_powers:
                max_count_powers = current_count_powers
                max_powers_index = i
        # Вывод столбца матрицы
        print(f"Искомый столбец [{max_powers_index:.7g}]")
        for string in matrix:
            print(f"{string[max_powers_index]:^1.7g}")
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
