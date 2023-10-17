# Задание статических входных данных
a = [-7, -6, -5, -4, -3, -1,  -2, -1, 2, 3]

# Объявление переменных
i = 1
out = []
longest = []
while i < len(a):
    flag = True
    for j in range(2, int(abs(a[i])**0.5)+1):  # Проверка текущего числа на простоту
        if a[i] % j == 0:
            flag = False
            break
    for j in range(2, int(abs(a[i-1])**0.5)+1):  # Проверка предыдущего числа на простоту
        if a[i-1] % j == 0:
            flag = False
            break
    if abs(a[i]) == 1 or abs(a[i-1]) == 1:
        flag = False
    if a[i - 1] < a[i] < 0 and flag:  # Проверка на начало последовательности
        out = [a[i-1]]
        while a[i - 1] < a[i] < 0 and flag:  # Пока элементы соответствуют критериям последовательности
            out.append(a[i])
            i += 1
            if i < len(a):  # Если не исходная последовательность закончилась
                for i in range(2, int(abs(a[i]) ** 0.5) + 1):
                    if a[i] % i == 0:
                        flag = False
                        break
                if abs(a[i]) == 1:
                    break
            else:
                break
    else:
        if len(longest) < len(out):  # Проверка для нахождения наибольшей подпоследовательности
            longest = out.copy()
        i += 1
if len(longest) < len(out):  # Проверка в случае если подпоследовательность заканчивается вместе с последовательностью
    longest = out.copy()

# Вывод
print(*longest)
