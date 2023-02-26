from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    red_v, blue_v = v
    visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] = 1

    while queue:
        red_v, blue_v = queue.popleft()
        if visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] > 11:
            return -1
        elif matrix[red_v[0]][red_v[1]] == 'O':
            return visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] - 1
        for i in range(4):
            next_red = (red_v[0], red_v[1])
            next_blue = (blue_v[0], blue_v[1])
            red_distance = 0
            blue_distance = 0

            while True:
                red_distance += 1
                next_red = (next_red[0] + dy[i], next_red[1] + dx[i])
                if matrix[next_red[0]][next_red[1]] == '#':
                    next_red = (next_red[0] - dy[i], next_red[1] - dx[i])
                    break
                elif matrix[next_red[0]][next_red[1]] == 'O':
                    break
            while True:
                blue_distance += 1
                next_blue = (next_blue[0] + dy[i], next_blue[1] + dx[i])
                if matrix[next_blue[0]][next_blue[1]] == '#':
                    next_blue = (next_blue[0] - dy[i], next_blue[1] - dx[i])
                    break
                elif matrix[next_blue[0]][next_blue[1]] == 'O':
                    break
            
            if matrix[next_blue[0]][next_blue[1]] != 'O':
                if next_red == next_blue:
                    if red_distance < blue_distance:
                        next_blue = (next_blue[0] - dy[i], next_blue[1] - dx[i])
                    else:
                        next_red = (next_red[0] - dy[i], next_red[1] - dx[i])
                if not visited[next_red[0]][next_red[1]][next_blue[0]][next_blue[1]]:
                    visited[next_red[0]][next_red[1]][next_blue[0]][next_blue[1]] = visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] + 1
                    queue.append((next_red, next_blue))
    
    return -1

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            red = (i, j)
        elif matrix[i][j] == 'B':
            blue = (i, j)

print(bfs((red, blue)))