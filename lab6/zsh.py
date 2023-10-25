# Ввод пользователя
a = list(map(int, input("Введите элементы списка через пробел: ").split()))

i = 2
out = []
longest = []


def IsFib(n):
    a, b = 0, 1
    for __ in range(n):
        a, b = b, a + b
        if n == b:
          return True
    return False


while i < len(a):
    if IsFib(a[i]) and IsFib(a[i-1]) and IsFib(a[i-2]):
        if a[i] == a[i-1] + a[i-2]:
            out = [a[i-2], a[i-1]]
            while i < len(a) and (a[i] == a[i-1] + a[i-2]):
                out.append(a[i])
                i += 1
            else:
                if len(out) > len(longest):
                    longest = out.copy()
    else:
        i += 1
print(*longest)
