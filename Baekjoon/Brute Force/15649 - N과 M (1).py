import sys

input = sys.stdin.readline

def dfs(array):
    if len(array) == m:
        print(*array)
        return

    for next_v in range(1, n + 1):
        if next_v not in array:
            dfs(array + [next_v])

n, m = map(int, input().split())

dfs([])