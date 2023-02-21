from collections import defaultdict
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

n, m, x = map(int, input().split())
graph = defaultdict(list)
answers = defaultdict(int)

for _ in range(m):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))

for i in range(1, n + 1):
    distance = defaultdict(lambda: inf)
    dijkstra(i)
    answers[i] += distance[x]

distance = defaultdict(lambda: inf)
dijkstra(x)

print(max([answers[i] + distance[i] for i in range(1, n + 1)]))