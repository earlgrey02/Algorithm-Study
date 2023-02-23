import heapq
import sys

input = sys.stdin.readline

def topological_sort():
    heap = sorted(filter(lambda x: indegree[x] == 0, indegree.keys()))

    while heap:
        v = heapq.heappop(heap)
        answer.append(v)
        for next_v in graph[v]:
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                heapq.heappush(heap, next_v)

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