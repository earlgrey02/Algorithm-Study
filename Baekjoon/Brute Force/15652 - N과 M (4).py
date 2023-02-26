import sys

input = sys.stdin.readline

def dfs(array):
    if len(array) == m:
        print(*array)
        return

    for next_v in range(array[-1] if array else 1, n + 1):
        dfs(array + [next_v])

n, m = map(int, input().split())

dfs([])