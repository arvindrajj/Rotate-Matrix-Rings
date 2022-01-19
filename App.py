def inc(index, row):
    index = (index + 1) % len(row)
    return index


def rotate_matrix(matrix, m, n, r):
    mat = []
    k = min(m, n) // 2  # compute no of layers
    for i in range(k):
        temp = []
        for j in range(i, n-1-i):
            temp.append(matrix[i][j])
        for j in range(i, m-1-i):
            temp.append(matrix[j][n-1-i])
        for j in range(n-1-i, i, -1):
            temp.append(matrix[m-1-i][j])
        for j in range(m-1-i, i, -1):
            temp.append(matrix[j][i])
        mat.append(temp)

    for i in range(k):
        row = mat[i]
        index = - r % len(row)
        if len(row) <= r:
            break

        for j in range(i, n-1-i):
            matrix[i][j] = row[index]
            index = inc(index, row)
        for j in range(i, m-1-i):
            matrix[j][n-1-i] = row[index]
            index = inc(index, row)

        for j in range(n-1-i, i, -1):
            matrix[m-1-i][j] = row[index]
            index = inc(index, row)

        for j in range(m-1-i, i, -1):
            matrix[j][i] = row[index]
            index = inc(index, row)

    for row in matrix:
        print(*row)


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(m)]
r = int(input())
rotate_matrix(matrix, m, n, r)

# input
# 4 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 3
