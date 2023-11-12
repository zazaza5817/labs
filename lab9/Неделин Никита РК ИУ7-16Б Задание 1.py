# Неделин Никита ИУ7-16Б
# Вариант 2
# Задание 1


# Ввод
n = list(map(int, input("Введите элементы первого списка через пробел: ").split()))
m = list(map(int, input("Введите элементы второго списка через пробел: ").split()))

# Инициализация двух указателей (на индексы двух списков)
ptr_n = 0
ptr_m = 0
# Создание нового списка
out_list = [0] * (len(n) + len(m))
# Заполнение нового списка
while ptr_n < len(n) and ptr_m < len(m):
    # Выбор наименьшего элемента и сдвиг указателя на список из которого выбран элемент
    if n[ptr_n] < m[ptr_m]:
        out_list[ptr_n + ptr_m] = n[ptr_n]
        ptr_n += 1
    else:
        out_list[ptr_n + ptr_m] = m[ptr_m]
        ptr_m += 1
# Дополнительная запись элементов второго списка в выходной список
while ptr_n < len(n):
    out_list[ptr_n + ptr_m] = n[ptr_n]
    ptr_n += 1
while ptr_m < len(m):
    out_list[ptr_n + ptr_m] = m[ptr_m]
    ptr_m += 1

# Вывод полученного списка
print("Полученный список:")
for elem in out_list:
    print(f"{elem:.5g}", end=" ")
print()

min_positive = float("+inf")
min_positive_i = -1
max_negative = float("-inf")
max_negative_i = -1
for i in range(len(out_list)):
    if 0 < out_list[i] < min_positive:
        min_positive = out_list[i]
        min_positive_i = i
    if 0 > out_list[i] > max_negative:
        max_negative = out_list[i]
        max_negative_i = i
if max_negative != float("-inf") and min_positive != float("+inf"):
    out_list[max_negative_i], out_list[min_positive_i] = out_list[min_positive_i], out_list[max_negative_i]
else:
    print(
        "Невозможно поменять элементы местами т.к. не существует хотя бы одного элемента подходящим под одно или оба "
        "условия")
