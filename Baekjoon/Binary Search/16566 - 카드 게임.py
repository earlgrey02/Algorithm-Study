from bisect import bisect_right
import sys

input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 != v2:
        parent[v2] = v1

n, m, k = map(int, input().split())
cards = sorted(map(int, input().split()))
parent = [i for i in range(n + 1)]

for num in list(map(int, input().split())):
    idx = bisect_right(cards, num)
    parent_idx = find(idx)
    print(cards[parent_idx])
    union(parent_idx + 1, parent_idx)