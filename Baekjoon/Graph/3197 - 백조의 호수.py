from collections import deque
import sys

input = sys.stdin.readline

def swan_bfs():
    next_swans = deque()

    while swans:
        v = swans.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if next_v == swan:
                return None
            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and not swan_visited[next_v[0]][next_v[1]]:
                swan_visited[next_v[0]][next_v[1]] = True
                if matrix[next_v[0]][next_v[1]] == 'X':
                    next_swans.append(next_v)
                else:
                    swans.append(next_v)
    
    return next_swans

def ice_bfs():
    next_ice = deque()
    
    while ice:
        v = ice.popleft()
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and not ice_visited[next_v[0]][next_v[1]]:
                ice_visited[next_v[0]][next_v[1]] = True
                if matrix[next_v[0]][next_v[1]] == 'X':
                    next_ice.append(next_v)
                else:
                    ice.append(next_v)
    
    return next_ice

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
swan_visited = [[False for _ in range(c)] for _ in range(r)]
ice_visited = [[False for _ in range(c)] for _ in range(r)]
swans = deque()
ice = deque()
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(r):
    if len(swans) >= 2:
        break
    for j in range(c):
        if matrix[i][j] == 'L':
            swans.append((i, j))
            matrix[i][j] = '.'

swan = swans.pop()

for i in range(r):
    for j in range(c):
        if matrix[i][j] == '.' and not ice_visited[i][j]:
            queue = deque([(i, j)])
            ice_visited[i][j] = True
            while queue:
                v = queue.popleft()
                for k in range(4):
                    next_v = (v[0] + dy[k], v[1] + dx[k])
                    if 0 <= next_v[0] < r and 0 <= next_v[1] < c and not ice_visited[next_v[0]][next_v[1]]:
                        ice_visited[next_v[0]][next_v[1]] = True
                        if matrix[next_v[0]][next_v[1]] == 'X':
                            ice.append(next_v)
                        else:
                            queue.append(next_v)

while True:
    swans = swan_bfs()
    if swans is None:
        break

    for i, j in ice:
        matrix[i][j] = '.'

    ice = ice_bfs()
    answer += 1

print(answer)