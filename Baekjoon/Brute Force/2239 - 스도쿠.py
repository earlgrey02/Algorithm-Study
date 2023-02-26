import sys

input = sys.stdin.readline

def check(row, column, n):
    for i in range(9):
        if (matrix[row][i] == n or matrix[i][column] == n):
            return False

    for i in range(3):
        for j in range(3):
            if (matrix[(row // 3) * 3 + i][(column // 3) * 3 + j] == n):
                return False

    return True

def dfs(depth):
    if depth == len(blank):
        for row in matrix:
            for i in row:
                print(i, end="")
            print()
        exit()

    for i in range(1, 10):
        row = blank[depth][0]
        column = blank[depth][1]
        if check(row, column, i):
            matrix[row][column] = i
            dfs(depth + 1)
            matrix[row][column] = 0

matrix = [list(map(int, input().strip())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]

dfs(0)