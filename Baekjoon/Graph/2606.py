from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

n, m = [int(input()) for _ in range(2)]
graph = defaultdict(list)
visited = defaultdict(lambda: False)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

bfs(1)

print(len(list(filter(lambda x: x, visited.values()))) - 1)