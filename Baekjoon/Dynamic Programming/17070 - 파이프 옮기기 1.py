import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    if matrix[0][i] == 1:
        break
    dp[0][i] = [1, 0, 0]

for i in range(1, n):
    for j in range(2, n):
        for k in range(3):
            if k == 0 and matrix[i][j] != 1:
                dp[i][j][k] += sum(dp[i][j - 1][::2])
            elif k == 1 and matrix[i][j] != 1:
                dp[i][j][k] += sum(dp[i - 1][j][1:])
            elif k == 2 and matrix[i][j] != 1 and matrix[i - 1][j] != 1 and matrix[i][j - 1] != 1:
                dp[i][j][k] += sum(dp[i - 1][j - 1][:])

print(sum(dp[-1][-1])) 