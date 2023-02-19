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
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answers = []

for rain in range(max(map(max, matrix))):
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > rain and not visited[i][j]:
                answer += 1
                bfs((i, j))

    answers.append(answer)

print(max(answers))