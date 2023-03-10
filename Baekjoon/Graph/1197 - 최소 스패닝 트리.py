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

    for start, end, w in edges:
        if find(start) != find(end):
            answer += w
            union(start, end)

v, e = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])
parent = [i for i in range(v + 1)]
rank = [0 for _ in range(v + 1)]
answer = 0

kruskal()

print(answer)