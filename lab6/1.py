# 1a
a = [1, 2, 3, 4, 5, 6, 7, 8]
a.insert(3, "inserted")
print(a)

# 1b
a = [1, 2, 3, 4, 5, 6, 7, 8]
index = 3
obj = "inserted"
a.append('')
for i in range(len(a)-1, index, -1):
    a[i] = a[i-1]
a[index] = obj
print(a)
