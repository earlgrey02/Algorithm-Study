import sys

input = sys.stdin.readline

def dfs(visited):
    if len(visited) == m:
        print(*visited)
        return

    for next_v in range(1, n + 1):
        if next_v not in visited:
            dfs(visited + [next_v])

n, m = map(int, input().split())

dfs([])