n = int(input("Введите n:"))
matrix = [[1+(i+j*n) for i in range(n)] for j in range(n)]
while True:
    print("Текущая матрица:")
    for string in matrix:
        for number in string:
            print(f"{number:^10.7g}", end="")
        print()
    direction = int(input("-1 - против часовой, 1 по часовой: "))
    if direction == -1:
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = tmp
    else:
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
