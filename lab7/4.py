# варианты по заданиям 5 5 7 5
# Неделин Никита ИУ7-16Б
# Программа для обработки строковых списков (Замена всех цифр на пробелы)
# Ввод
n = int(input("Введите кол-во элементов списка: "))
a = [""]*n
for i in range(n):
    a[i] = input(f"Введите {i+1}-ый элементы списка: ")
print(a)


# Обработка
numbers = list(map(str, range(10)))  # Генерация всех цифр
for i in range(len(a)):  # Проход по всем элементам списка
    for number in numbers:  # Проход по всем цифрам
        result_str = ""
        for char in a[i]:
            if char not in numbers:
                result_str += char
            else:
                result_str += " "
        a[i] = result_str
        # a[i] = a[i].replace(number, " ")  # Замена каждой цифры на пробел в текущем элементе


# Вывод списка
print(a)
