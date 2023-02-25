from itertools import combinations
from math import inf
import sys

input = sys.stdin.readline

def dfs(v, depth, cnt):
    global answer

    if depth == 3:
        answer = max(answer, cnt)
        return
    for i in range(4):
        next_v = (v[0] + dy[i], v[1] + dx[i])
        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and depth < 3 and not visited[next_v[0]][next_v[1]]:
            visited[next_v[0]][next_v[1]] = True
            dfs(next_v, depth + 1, cnt + matrix[next_v[0]][next_v[1]])
            visited[next_v[0]][next_v[1]] = False

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = -inf

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs((i, j), 0, matrix[i][j])
        visited[i][j] = False

        for a in combinations(range(4), 3):
            temp = matrix[i][j]
            for b in a:
                next_v = (i + dy[b], j + dx[b])
                if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
                    temp += matrix[next_v[0]][next_v[1]]
            answer = max(answer, temp)

print(answer)