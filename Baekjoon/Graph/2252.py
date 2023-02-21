from collections import deque
import sys

input = sys.stdin.readline

def topological_sort():
    queue = deque(list(map(lambda x: x[0], filter(lambda x: x[1] == 0, indegree.items()))))
    
    while queue:
        v = queue.popleft()
        answer.append(v)
        for next_v in graph[v]:
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                queue.append(next_v)

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
indegree = {i: 0 for i in range(1, n + 1)}
answer = []

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1

topological_sort()

print(*answer)