import sys

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

floyd_warshall()

for i in range(n):
    print(*graph[i])