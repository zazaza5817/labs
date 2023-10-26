# варианты по заданиям 5 5 7 5
# Неделин Никита ИУ7-16Б
# Программа для обработки целочисленных списков (Замена всех чисел на пробелы)
# Ввод
n = int(input("Введите кол-во элементов списка: "))
a = [""]*n
for i in range(n):
    a[i] = input(f"Введите {i+1}-ый элементы списка: ")
print(a)


# Обработка
numbers = list(map(str, range(10)))
for i in range(len(a)):
    for number in numbers:
        a[i] = a[i].replace(number, " ")


# Вывод списка
print(a)
