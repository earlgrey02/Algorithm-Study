from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        if v == ''.join([str(i) for i in range(1, 10)]):
            return visited[v]
        idx = v.find('9')
        y, x = idx // 3, idx % 3
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 3 and 0 <= nx < 3:
                next_v = list(v)
                next_v[idx], next_v[ny * 3 + nx] = next_v[ny * 3 + nx], next_v[idx]
                next_v = ''.join(next_v)
                if not visited[next_v]:
                    visited[next_v] = visited[v] + 1
                    queue.append(next_v)
    
    return -1

string = ''.join([''.join(input().split()) for _ in range(3)]).replace('0', '9')
visited = defaultdict(lambda: 0)
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

print(bfs(string))