from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    cnt = 1

    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < m and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                cnt += 1
                queue.append(next_v)
    
    return cnt

m, n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
answer = []
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            matrix[i][j] = 1

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and not visited[i][j]:
            answer.append(bfs((i, j)))

print(len(answer))
print(*sorted(answer))