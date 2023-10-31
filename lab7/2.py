# варианты по заданиям 5 5 7 5
# Неделин Никита ИУ7-16Б
# Программа для обработки целочисленных списков (Вставки после каждого отрицательного элемента его удвоенного значения)
# Ввод
a = list(map(int, input("Введите элементы списка через пробел: ").split()))


# Инициализация числа элементов и количества отрицательных из них
elms_count = len(a)
negative_count = 0
# Обработка списка
for i in a:
    if i < 0:
        negative_count += 1
a.extend([0]*negative_count)
write_index = elms_count + negative_count - 1
read_index = elms_count - 1
while read_index > 0:  # Проходимся по всем заданным пользователем элементам справа налево
    if a[read_index] < 0:  # Если встретили отрицательный элемент
        # Записываем удвоенное текущее считываемое значение в ячейку с текущим индексом записи
        a[write_index] = a[read_index] * 2
        a[write_index-1] = a[read_index]  # Записываем текущее считываемое значение в следующую ячейку
        write_index -= 2  # Смещаем индекс ячейки для записи на 2 т.к. записали два элемента
    else:  # Если встретили не отрицательный элемент
        a[write_index] = a[read_index]  # Записываем текущее считываемое значение в ячейку с текущим индексом записи
        write_index -= 1  # Смещаем индекс ячейки для записи на 1 т.к. записали один элемент
    read_index -= 1  # Смещаем индекс ячейки для чтения на 1 т.к. обработали один элемент


# Вывод
print(a)
