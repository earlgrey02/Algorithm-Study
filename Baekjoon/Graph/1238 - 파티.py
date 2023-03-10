from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(v, graph):
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

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))
    reversed_graph[end].append((start, w))

distance = dijkstra(x, graph)
reversed_distance = dijkstra(x, reversed_graph)

print(max([reversed_distance[i] + distance[i] for i in range(1, n + 1) if i != x]))