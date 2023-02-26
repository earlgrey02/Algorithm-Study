import sys

input = sys.stdin.readline


def dfs(total, depth):
    global answer, s

    if depth == n:
        if total == s:
            answer += 1
        return
    
    dfs(total + array[depth], depth + 1)
    dfs(total, depth + 1)

n, s = map(int, input().split())
array = list(map(int, input().split()))
answer = 0

dfs(0, 0)

print(answer if s != 0 else answer - 1)