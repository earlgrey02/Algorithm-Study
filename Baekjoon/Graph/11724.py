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

n, m = map(int, input().split())
graph = defaultdict(list)
visited = defaultdict(lambda: False)
answer = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n + 1):
    if not visited[i]:
        answer += 1
        bfs(i)

print(answer)