from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([(v, 0)])
    visited[v] = v

    while queue:
        v, cnt = queue.popleft()
        if v == k:
            print(cnt)
            return cnt
        for next_v in [v + 1, v - 1, v * 2]:
            if 0 <= next_v <= 100000 and visited[next_v] == -1:
                visited[next_v] = v
                queue.append((next_v, cnt + 1))

n, k = map(int, input().split())
visited = [-1] * 100001
path = []

cnt = bfs(n)

for i in range(cnt + 1):
    path.append(k)
    k = visited[k]

print(*path[::-1])