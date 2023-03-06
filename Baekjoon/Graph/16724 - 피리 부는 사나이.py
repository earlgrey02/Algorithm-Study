import sys

input = sys.stdin.readline

def dfs(v):
    global answer

    idx = direction.index(matrix[v[0]][v[1]])
    next_v = (v[0] + dy[idx], v[1] + dx[idx])
    
    if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
        if not visited[next_v[0]][next_v[1]]:
            visited[next_v[0]][next_v[1]] = 1
            dfs(next_v)
        elif visited[next_v[0]][next_v[1]] == 1:
            answer += 1

    visited[v[0]][v[1]] = 2

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
direction = ('D', 'U', 'R', 'L')
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs((i, j))

print(answer)