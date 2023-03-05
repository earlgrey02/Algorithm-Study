from math import inf
import sys

input = sys.stdin.readline

def init(start, end, idx):
    if start == end:
        tree[idx][0] = array[start - 1]
        tree[idx][1] = array[start - 1]
        return tree[idx]
    
    mid = (start + end) // 2
    temp = [init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1)]
    tree[idx][0] = max(temp[0][0], temp[1][0])
    tree[idx][1] = min(temp[0][1], temp[1][1])

    return tree[idx]

def find(start, end, idx, left, right):
    if right < start or end < left:
        return [-inf, inf]
    elif left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    temp = [find(start, mid, idx * 2, left, right), find(mid + 1, end, idx * 2 + 1, left, right)]
    return [max(temp[0][0], temp[1][0]), min(temp[0][1], temp[1][1])]

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
tree = [[0 for _ in range(2)] for _ in range(n * 4)]

init(1, n, 1)

for _ in range(m):
    a, b = map(int, input().split())

    print(*reversed(find(1, n, 1, a, b)))