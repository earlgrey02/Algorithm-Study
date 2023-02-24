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
        for next_v, next_w in [(v - 1, 1), (v + 1, 1), (v * 2, 0)]:
            next_w += w
            if 0 <= next_v <= 100000 and next_w < distance[next_v]:
                distance[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))

n, k = map(int, input().split())
distance = defaultdict(lambda: inf)

dijkstra(n)

print(distance[k])