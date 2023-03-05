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
            
n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]
answer = 0

for i in range(m):
    start, end = map(int, input().split())

    if answer:
        continue

    if find(start) == find(end):
        answer = i + 1
    else:
        union(start, end)

print(answer)