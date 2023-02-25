from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] > rain and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
rain = 0
answer = 0
cnt = 1
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while cnt > 0:
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > rain and not visited[i][j]:
                bfs((i, j))
                cnt += 1
    
    answer = max(answer, cnt)
    rain += 1

print(answer)