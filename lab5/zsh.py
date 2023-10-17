N = int(input("N="))
m = []
# for _ in range(N):
#     m.append([0]*N)
m = [[0] * N for _ in range(N)]
mean = N // 2
i = 0
j = 0
cnt = 1
iters = -1


def function(i, j, mean, N):
    if N % 2 != 0:
        return (i, j) != (mean, mean)
    else:
        return (i, j) != (mean, mean -1)


while function(i, j, mean, N):
    iters += 1
    while j < N - 1 - iters:
        m[i][j] = cnt
        cnt += 1
        j += 1
    while i < (N - 1 - iters):
        m[i][j] = cnt
        cnt += 1
        i += 1
    while j > iters:
        m[i][j] = cnt
        cnt += 1
        j -= 1
    while i > iters + 1:
        m[i][j] = cnt
        cnt += 1
        i -= 1
m[i][m[i].index(0)] = cnt

for g in m:
    for a in g:
        print(a, end="\t")
    print(g)
