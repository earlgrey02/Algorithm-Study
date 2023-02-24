import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    for next_v, next_w in graph[v]:
        if not visited[next_v]:
            visited[next_v] = visited[v] + next_w
            dfs(next_v)

n = int(input())
graph = {i: [] for i in range(1, n + 1)}
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))
    graph[end].append((start, w))

visited[1] = 1
dfs(1)
v = visited.index(max(visited))
visited = [0 for _ in range(n + 1)]
visited[v] = 1
dfs(v)

print(max(visited) - 1)