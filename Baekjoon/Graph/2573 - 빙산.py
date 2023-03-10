from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    ice = set()
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()
        melt = 0
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                if matrix[next_v[0]][next_v[1]] > 0:
                    visited[next_v[0]][next_v[1]] = True
                    queue.append(next_v)
                else:
                    melt += 1
        if melt:
            ice.add(((v[0], v[1]), melt))
    
    return ice

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                cnt += 1
                ice = bfs((i, j))
                while ice:
                    v, melt = ice.pop()
                    matrix[v[0]][v[1]] -= melt
    
    if cnt > 1:
        break
    elif cnt == 0:
        answer = 0
        break
    answer += 1

print(answer)