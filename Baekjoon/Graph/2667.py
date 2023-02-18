from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    count = 0

    while queue:
        v = queue.popleft()
        count += 1
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)
    
    return count

n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] and not visited[i][j]:
            answer.append(bfs((i, j)))

print(len(answer))
for i in sorted(answer):
    print(i)