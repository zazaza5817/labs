# варианты по заданиям 5 5 7 5
# Неделин Никита ИУ7-16Б
# Программа для обработки целочисленных списков (Нахождение строки без пробелов максимальной длины)
# Ввод
n = int(input("Введите кол-во элементов списка: "))
a = [""]*n
for i in range(n):
    a[i] = input(f"Введите {i+1}-ый элементы списка: ")
print(a)


# Инициализация переменных максимально длины и индекса элемента с этой длиной
maxLen = 0
maxI = -1
# Нахождение элемента с максимальной длиной без пробелов списке
for i in range(len(a)):
    length = 0
    for letter in a[i]:
        length += 1
        if letter == " ":
            break
    else:
        if length > maxLen:
            maxLen = length
            maxI = i


# Если в списке есть искомый элемент
if maxI >= 0:
    print(a[maxI])
else:
    print("Нет ни одного элемента удовлетворяющего условиям")

