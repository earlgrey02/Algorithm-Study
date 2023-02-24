from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    fishes = []

    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] <= size and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                if 0 < matrix[next_v[0]][next_v[1]] < size:
                    fishes.append((*next_v, visited[next_v[0]][next_v[1]]))
                queue.append(next_v)
    
    return sorted(fishes, key=lambda x: (x[2], x[0], x[1]))

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
size = 2
exp = 0
answer = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            shark = (i, j)
            matrix[i][j] = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    fishes = bfs(shark)
    if not fishes:
        break
    fish = fishes[0]
    answer += fish[2]
    shark = tuple(fish[:2])
    matrix[fish[0]][fish[1]] = 0
    exp += 1
    if size == exp:
        exp = 0
        size += 1

print(answer)