from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()
        for i in range(8):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < h and 0 <= next_v[1] < w and matrix[next_v[0]][next_v[1]] == 1 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    answer = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                answer += 1
                bfs((i, j))
    
    print(answer)