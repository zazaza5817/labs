a = [1, 2, 3, 4, 5, 4, 3, 2, 1]

i = 1
while i < len(a)-1:
    if a[i-1] > a[i] < a[i+1]:
        print(a[i])
    elif a[i-1] < a[i] > a[i+1]:
        print(a[i])
    i += 1
