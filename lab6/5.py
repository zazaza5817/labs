# Ввод пользователя
a = list(map(int, input("Введите элементы списка через пробел: ").split()))


# Нахождение индексов элементов, которых необходимо поменять местами
first_index = 0
second_index = 0
last_min = float("inf")
for i in range(len(a)):
    if a[i] % 2 == 0:
        first_index = i
    if 0 < a[i] < last_min:
        last_min = a[i]
        second_index = i
# Смена элементов местами
temp = a[first_index]
a[first_index] = a[second_index]
a[second_index] = temp

# Вывод
print(a)
