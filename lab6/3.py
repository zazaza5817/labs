a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
k = int(input("Введите К: "))

i = 1
extr = []
while i < len(a)-1:
    if a[i-1] > a[i] < a[i+1]:
        extr.append(a[i])
    elif a[i-1] < a[i] > a[i+1]:
        extr.append(a[i])
    i += 1
if k > len(extr):
    print("Не существует экстремума с таким номером")
elif k < 1:
    print("Значение номера экстремума должно быть больше нуля")
else:
    print(extr[k-1])
