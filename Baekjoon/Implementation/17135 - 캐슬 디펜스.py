from collections import deque
import sys

input = sys.stdin.readline

def bfs(v, matrix):
    queue = deque([v])
    visited = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    while queue:
        v = queue.popleft()
        for i in range(3):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                if visited[next_v[0]][next_v[1]] <= d:
                    if matrix[next_v[0]][next_v[1]] == 1:
                        return next_v
                    else:
                        queue.append(next_v)
    
    return

def dfs(v, depth):
    if depth == 3:
        idxs.append(v)
        return
    
    for i in range(v[-1] if v else 0, m):
        if i not in v:
            dfs(v + [i], depth + 1)

n, m, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
idxs = []
answers = []
dy = (0, -1, 0)
dx = (-1, 0, 1)

dfs([], 0)

for archers in [[(n, j) for j in i] for i in idxs]:
    matrix_copy = [row[:] for row in matrix]
    answer = 0
    
    while True:
        end = True
        enemies = set()

        for archer in archers:
            enemy = bfs(archer, matrix_copy)
            if enemy:
                enemies.add(enemy)

        answer += len(set(enemies))

        for i, j in enemies:
            matrix_copy[i][j] = 0
        for i in range(n - 1, 0, -1):
            matrix_copy[i] = matrix_copy[i - 1]
        matrix_copy[0] = [0 for _ in range(m)]

        for i in range(n):
            if not end:
                break
            for j in range(m):
                if matrix_copy[i][j] == 1:
                    end = False
                    break

        if end:
            break

    answers.append(answer)

print(max(answers))