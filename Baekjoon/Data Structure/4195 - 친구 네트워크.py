from collections import defaultdict
import sys

input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 != v2:
        parent[v1] = v2
        distance[v2] += distance[v1]

t = int(input())

for _ in range(t):
    f = int(input())
    parent = {}
    distance = defaultdict(lambda: 1)
    
    for _ in range(f):
        f1, f2 = input().strip().split()
        if f1 not in parent:
            parent[f1] = f1
        if f2 not in parent:
            parent[f2] = f2
        union(f1, f2)

        print(distance[find(f1)])