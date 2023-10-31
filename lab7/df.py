# Неделин Никита ИУ7-16Б
# Вводится список строк. Найти и вывести строки, где количество латинских букв равно сумме всех цифр.
# Ввод
n = int(input("Введите кол-во элементов списка: "))
a = [""]*n
for i in range(n):
    a[i] = input(f"Введите {i+1}-ый элементы списка: ")


latin_alphabet = [chr(i) for i in range(ord("a"), ord('z') + 1)]
numbers = list(map(str, range(10)))
for string in a:
    latin_letters_count = 0
    numbers_sum = 0
    for char in string.lower():
        if char in latin_alphabet:
            latin_letters_count += 1
        elif char in numbers:
            numbers_sum += int(char)
    if numbers_sum == latin_letters_count:
        print(string)
