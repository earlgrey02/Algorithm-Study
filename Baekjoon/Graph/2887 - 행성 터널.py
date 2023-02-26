import sys

input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 != v2:
        if rank[v1] == rank[v2]:
            parent[v2] = v1
            rank[v1] += 1
        elif rank[v1] < rank[v2]:
            parent[v1] = v2
        else:
            parent[v2] = v1

def kruskal():
    global answer

    for edge in edges:
        start, end, w = edge
        if find(start) != find(end):
            answer += w
            union(start, end)

n = int(input())
planets = [tuple(map(int, input().split())) for _ in range(n)]
planet_pos = [sorted(list(map(lambda x: (x[0], x[1][i]), enumerate(planets))), key=lambda x: x[1]) for i in range(3)]
edges = []
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]
answer = 0

for i in range(3):
    for j in range(n - 1):
        start, end, w = planet_pos[i][j][0], planet_pos[i][j + 1][0], abs(planet_pos[i][j][1] - planet_pos[i][j + 1][1])
        edges.append((start, end, w))

edges.sort(key=lambda x: x[2])
kruskal()

print(answer)