# 1a
a = list(map(int, input("Введите элементы списка через пробел: ").split()))
index = int(input("Введите индекс: "))
if 0 <= index <= len(a)+1:
    obj = int(input("Введите объект для вставки: "))
    a.insert(index, obj)
    print(a)
else:
    print("Индекс не находится в списке")

# 1b
a = list(map(int, input("Введите элементы списка через пробел: ").split()))
index = int(input("Введите индекс: "))
if 0 <= index <= len(a) + 1:
    obj = int(input("Введите число для вставки: "))
    a.append('')
    for i in range(len(a)-1, index, -1):
        a[i] = a[i-1]
    a[index] = obj
    print(a)
else:
    print("Индекс не находится в списке")
