from math import inf
import sys

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

n, m = map(int, input().split())
graph = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end = map(lambda x: int(x) - 1, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

floyd_warshall()

print(min(enumerate(map(sum, graph)), key=lambda x: x[1])[0] + 1)