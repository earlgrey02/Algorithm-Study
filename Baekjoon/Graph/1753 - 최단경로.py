from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(v):
    heap = []
    heapq.heappush(heap, (0, v))
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

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distance = [inf for _ in range(v + 1)]

for _ in range(e):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))

dijkstra(k)

print(*[distance[i] if distance[i] != inf else "INF" for i in range(1, v + 1)], sep="\n")