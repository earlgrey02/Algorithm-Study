import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 != v2:
        parent[v1] = v2

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")