import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    if dp[v[0]][v[1]]:
        return dp[v[0]][v[1]] + 1
    dp[v[0]][v[1]] = 1

    for i in range(4):
        next_v = (v[0] + dy[i], v[1] + dx[i])
        if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[v[0]][v[1]] < matrix[next_v[0]][next_v[1]]:
            dp[v[0]][v[1]] = max(dp[v[0]][v[1]], dfs(next_v))

    return dp[v[0]][v[1]] + 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs((i, j))

print(max(map(max, dp)))