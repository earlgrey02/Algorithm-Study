from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque(v)
    
    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                matrix[next_v[0]][next_v[1]] = 1
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
tomatoes = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 1]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

bfs(tomatoes)

if len([0 for i in range(n) for j in range(m) if matrix[i][j] == 0]) >= 1:
    answer = -1
else:
    answer = max(map(max, visited))

print(answer)