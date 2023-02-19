from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = -visited[v]
                queue.append(next_v)
            elif visited[next_v] == visited[v]:
                return False

    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    visited = defaultdict(int)
    answer = "YES"

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, v + 1):
        if not visited[i] and not bfs(i):
            answer = "NO"
            break

    print(answer)