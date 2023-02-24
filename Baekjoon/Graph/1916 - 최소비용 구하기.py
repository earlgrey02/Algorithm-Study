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

n, m = [int(input()) for _ in range(2)]
graph = {i: [] for i in range(1, n + 1)}
distance = {i: inf for i in range(1, n + 1)}

for _ in range(m):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])