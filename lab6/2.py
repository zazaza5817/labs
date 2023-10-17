# 2a
a = [1, 2, 3, 4, 5, 6, 7, 8]
a.pop(3)
print(a)

# 2b
a = [1, 2, 3, 4, 5, 6, 7, 8]
index = 3
out = []
for i in range(index):
    out.append(a[i])
for i in range(index+1, len(a)):
    out.append(a[i])
print(out)
