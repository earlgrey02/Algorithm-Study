from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    count = 1

    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < m and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                count += 1
                queue.append(next_v)
    
    return count

m, n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
answers = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(k):
    point = list(map(int, input().split()))

    for i in range(point[1], point[3]):
        for j in range(point[0], point[2]):
            matrix[i][j] = 1

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and not visited[i][j]:
            answers.append(bfs((i, j)))

print(len(answers))
print(*sorted(answers))