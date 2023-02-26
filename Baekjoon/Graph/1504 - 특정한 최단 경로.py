from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(v):
    heap = []
    heapq.heappush(heap, (0, v))
    distance = [inf for _ in range(n + 1)]
    distance[v] = 0

    while heap:
        w, v = heapq.heappop(heap)
        if distance[v] < w:
            continue
        for next_v, next_w in graph[v]:
            next_w += w
            if next_w < distance[next_v]:
                distance[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))
    
    return distance

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))
    graph[end].append((start, w))

v1, v2 = map(int, input().split())
answer = min(dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n], dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n])

print(answer if answer != inf else -1)