from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    print(v, end=" ")

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                print(next_v, end=" ")
                visited[next_v] = True
                queue.append(next_v)

n, m, v = map(int, input().split())
graph = defaultdict(list)
visited = defaultdict(lambda: False)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph.keys():
    graph[key].sort()

dfs(v)
print()
visited = defaultdict(lambda: False)
bfs(v)