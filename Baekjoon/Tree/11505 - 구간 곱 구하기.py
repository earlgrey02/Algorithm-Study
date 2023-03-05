import sys

input = sys.stdin.readline

def init(start, end, idx):
    if start == end:
        tree[idx] = array[start - 1]
        return tree[idx]
    
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) * init(mid + 1, end, idx * 2 + 1) % 1000000007

    return tree[idx]

def find(start, end, idx, left, right):
    if right < start or end < left:
        return 1
    elif left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2

    return find(start, mid, idx * 2, left, right) * find(mid + 1, end, idx * 2 + 1, left, right) % 1000000007

def update(start, end, idx, key, value):
    if not start <= key <= end:
        return

    if start == end:
        tree[idx] = value
    else:
        mid = (start + end) // 2
        update(start, mid, idx * 2, key, value)
        update(mid + 1, end, idx * 2 + 1, key, value)
        tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % 1000000007

n, m, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n * 4)]

init(1, n, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        update(1, n, 1, b, c)
        array[b - 1] = c
    elif a == 2:
        print(find(1, n, 1, b, c))