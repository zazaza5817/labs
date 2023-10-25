# варианты по заданиям 5 5 7 5
# Неделин Никита ИУ7-16Б
# Программа для обработки целочисленных списков
# Ввод
a = list(map(int, input("Введите элементы списка через пробел: ").split()))


# Инициализация числа элементов и количества отрицательных из них
elms_count = len(a)
negative_count = 0
# Обработка списка
for i in a:
    if i < 0:
        negative_count += 1
a.extend(["empty"]*negative_count)
i = len(a) - 1
write_index = len(a) - 1
read_index = elms_count - 1
while read_index > 0:
    if a[read_index] < 0:
        a[write_index] = a[read_index] * 2
        a[write_index-1] = a[read_index]
        write_index -= 2
    else:
        a[write_index] = a[read_index]
        write_index -= 1
    read_index -= 1


# Вывод
print(a)
