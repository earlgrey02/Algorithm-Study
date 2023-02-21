from math import inf
import sys

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

n, m = [int(input()) for _ in range(2)]
graph = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end, w = map(int, input().split())
    graph[start - 1][end - 1] = min(graph[start - 1][end - 1], w)

floyd_warshall()

for row in [[i if i != inf else 0 for i in row] for row in graph]:
    print(*row)