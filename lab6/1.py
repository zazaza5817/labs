# 1a
a = [1, 2, 3, 4, 5, 6, 7, 8]
a.insert(3, "inserted")
print(a)

# 1b
a = [1, 2, 3, 4, 5, 6, 7, 8]
index = 2
obj = "inserted"
if 0 <= index <= len(a):
    a.append('')
    for i in range(len(a)-1, index, -1):
        a[i] = a[i-1]
    a[index] = obj
    print(a)
else:
    print("Индекс не находится в списке")
