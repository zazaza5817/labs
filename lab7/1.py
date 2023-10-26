# варианты по заданиям 5 5 7 5
# Неделин Никита ИУ7-16Б
# Программа для обработки целочисленных списков (удаление отрицательных элементов)
# Ввод
a = list(map(int, input("Введите элементы списка через пробел: ").split()))


# Инициализация индексов чтения и записи
read_index = 0
write_index = 0
not_deleted_count = len(a)
# Обработка по указанному правилу
while read_index < len(a):
    if a[read_index] >= 0:
        a[write_index] = a[read_index]
        write_index += 1
    else:
        not_deleted_count -= 1
    read_index += 1


# Вывод
a = a[:not_deleted_count]
print(a)
