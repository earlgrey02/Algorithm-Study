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
matrix = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            union(i + 1, j + 1)

print("YES" if len(set([find(i) for i in map(int, input().split())])) == 1 else "NO")