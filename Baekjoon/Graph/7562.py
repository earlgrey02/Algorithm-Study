from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = 1

    while queue:
        v = queue.popleft()
        if v == point:
            return visited[v[0]][v[1]]
        for i in range(8):
            temp = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= temp[0] < n and 0 <= temp[1] < n and not visited[temp[0]][temp[1]]:
                visited[temp[0]][temp[1]] = visited[v[0]][v[1]] + 1
                queue.append(temp)

t = int(input())
dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    n = int(input())
    v, point = [tuple(map(int, input().split())) for _ in range(2)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    print(bfs(v) - 1)