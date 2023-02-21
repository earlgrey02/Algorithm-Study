from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    union = [(v, matrix[v[0]][v[1]])]

    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and l <= abs(matrix[v[0]][v[1]] - matrix[next_v[0]][next_v[1]]) <= r and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                union.append((next_v, matrix[next_v[0]][next_v[1]]))
                queue.append(next_v)

    return union

n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = 0

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    end = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs((i, j))
                if len(union) != 1:
                    end = False
                    population = sum(map(lambda x: x[1], union)) // len(union)
                    for v in map(lambda x: x[0], union):
                        matrix[v[0]][v[1]] = population
    
    if end:
        break
    answer += 1

print(answer)