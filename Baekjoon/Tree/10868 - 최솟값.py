from math import inf
import sys

input = sys.stdin.readline

def init(start, end, idx):
    if start == end:
        tree[idx] = array[start - 1]
        return tree[idx]
    
    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))

    return tree[idx]

def find(start, end, idx, left, right):
    if right < start or end < left:
        return inf
    elif left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2

    return min(find(start, mid, idx * 2, left, right), find(mid + 1, end, idx * 2 + 1, left, right))

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n * 4)]

init(1, n, 1)

for _ in range(m):
    a, b = map(int, input().split())

    print(find(1, n, 1, a, b))