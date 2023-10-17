# 2a
a = list(map(int, input("Введите элементы списка через пробел: ").split()))
index = int(input("Введите индекс: "))
if 0 <= index < len(a):
    a.pop(index)
    print(a)
else:
    print("Индекс находится не в пределах списка")

# 2b
a = list(map(int, input("Введите элементы списка через пробел: ").split()))
index = int(input("Введите индекс: "))
if 0 <= index < len(a):
    for i in range(index+1, len(a)):
        a[i-1] = a[i]
    a.pop(-1)
    print(a)
else:
    print("Индекс находится не в пределах списка")
