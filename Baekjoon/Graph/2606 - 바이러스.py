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

n, m = [int(input()) for _ in range(2)]
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]
answer = 0

for _ in range(m):
    start, end = map(int, input().split())
    union(start, end)

for i in range(2, n + 1):
    if find(i) == find(1):
        answer += 1

print(answer)