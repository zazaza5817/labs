# Неделин Никита ИУ7-16Б
n = int(input("Введите кол-во столбцов матрицы "))
m = int(input("Введите кол-во строк матрицы "))
vowels = 'aeiouAEIOU'
if n > 0 and m > 0:
    # Инициализация матрицы
    matrix = [""]*m
    # Заполнение матрицы
    for i in range(m):
        string = input("Введите очередную строчку матрицы: ")
        if len(string) != n:
            print("Введена строчка, длина которой не соответствует длине строчки матрицы")
            break
        matrix[i] = string
    else:
        # Вывод исходной матрицы
        print("Введенная матрица")
        for string in matrix:
            print(string)
        # Обработка
        for i in range(m):
            # Создание новой строчки
            new_string = ""
            for char in matrix[i]:
                # Добавление элементов в новую строчку по условию
                if char not in vowels:
                    new_string += char
                else:
                    new_string += "."
            # Замена существующей строчки на новую
            matrix[i] = new_string
        # Вывод измененной матрицы
        print("Измененная матрица")
        for string in matrix:
            print(string)
else:
    print("Количество столбцов и количество строк матрицы должно быть больше нуля")
