from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = v
                queue.append(next_v)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

bfs(1)

print(*visited[2:], sep='\n')