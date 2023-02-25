from collections import deque
import sys

input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
    return visited

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n + 1):
    graph[i].sort()

dfs(v)
visited = [False for _ in range(n + 1)]
print()
bfs(v)