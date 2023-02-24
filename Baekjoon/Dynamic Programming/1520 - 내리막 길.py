import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    if v == (m - 1, n - 1):
        return 1 
    elif dp[v[0]][v[1]] != -1:
        return dp[v[0]][v[1]]

    dp[v[0]][v[1]] = 0

    for i in range(4):
        next_v = (v[0] + dy[i], v[1] + dx[i])
        if 0 <= next_v[0] < m and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] < matrix[v[0]][v[1]]:
            dp[v[0]][v[1]] += dfs(next_v)

    return dp[v[0]][v[1]]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

print(dfs((0, 0)))