from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijstra(v):
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

t = int(input())

for _ in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    answer = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    points = [int(input()) for _ in range(t)]
    distance_s, distance_g, distance_h = dijstra(s), dijstra(g), dijstra(h)

    for point in points:
        if (distance_s[g] + distance_g[h] + distance_h[point] == distance_s[point] or distance_s[h] + distance_h[g] + distance_g[point] == distance_s[point]) and distance_s[point] != inf:
            answer.append(point)
    
    print(*sorted(answer))