from collections import deque
import sys

input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 != v2:
        parent[v2] = v1

def civilization():
    global k

    while civils:
        v = civils.popleft()
        queue.append(v)
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] > 0 and find(matrix[v[0]][v[1]]) != find(matrix[next_v[0]][next_v[1]]) and matrix[v[0]][v[1]] != matrix[next_v[0]][next_v[1]]:
                union(matrix[v[0]][v[1]], matrix[next_v[0]][next_v[1]])
                k -= 1

def bfs():
    while queue:
        v = queue.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] == 0:
                matrix[next_v[0]][next_v[1]] = matrix[v[0]][v[1]]
                civils.append(next_v)

n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
civils = deque([tuple(i - 1 for i in map(int, input().split())) for _ in range(k)])
for i, v in enumerate(civils):
    matrix[v[0]][v[1]] = i + 1
parent = [i for i in range(k + 1)]
queue = deque()
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = 0

while k > 1:
    civilization()
    if k == 1:
        break
    bfs()
    answer += 1

print(answer)