from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        if v == 100:
            return visited[v] - 1
        for i in range(1, 7):
            next_v = v + i
            if 1 <= next_v <= 100 and not visited[next_v]:
                visited[next_v] = visited[v] + 1
                if snakes[next_v] or ladders[next_v]:
                    next_v = snakes[next_v] if snakes[next_v] else ladders[next_v]
                    if not visited[next_v]:
                        visited[next_v] = visited[v] + 1
                        queue.append(next_v)
                else:
                    queue.append(next_v)

n, m = map(int, input().split())
snakes = defaultdict(int)
ladders = defaultdict(int)
visited = [0 for _ in range(101)]

for _ in range(n):
    start, end = map(int, input().split())
    snakes[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    ladders[start] = end

print(bfs(1))