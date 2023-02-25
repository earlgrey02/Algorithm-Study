import sys

input = sys.stdin.readline

def bfs(v, visited):
    global answer
    queue = set([(v, visited)])
    
    while queue:
        v, visited = queue.pop()
        answer = max(answer, len(visited))
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])
            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] not in visited:
                queue.add((next_v, visited + matrix[next_v[0]][next_v[1]]))

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

bfs((0, 0), matrix[0][0])

print(answer)