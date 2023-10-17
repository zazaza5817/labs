a = list(map(int, input("Введите элементы списка через пробел").split()))
k = int(input("Введите К: "))

i = 1
cnt = 0
while i < len(a)-1:
    if a[i-1] > a[i] < a[i+1]:
        cnt += 1
        if cnt == k:
            print(a[i])
            break
    elif a[i-1] < a[i] > a[i+1]:
        cnt += 1
        if cnt == k:
            print(a[i])
            break
    i += 1
else:
    print("Не существует экстремума с таким номером")
