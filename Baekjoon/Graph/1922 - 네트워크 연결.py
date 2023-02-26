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

n, m = [int(input()) for _ in range(2)]
edges = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]
answer = 0

kruskal()

print(answer)