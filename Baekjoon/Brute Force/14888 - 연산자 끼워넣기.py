from math import inf
import sys

input = sys.stdin.readline

def dfs(total, depth):
    global answer

    if depth == n:
        answer[0] = max(answer[0], total)
        answer[1] = min(answer[1], total)
        return

    if operator[0] > 0:
        operator[0] -= 1
        dfs(total + array[depth], depth + 1)
        operator[0] += 1
    if operator[1] > 0:
        operator[1] -= 1
        dfs(total - array[depth], depth + 1)
        operator[1] += 1
    if operator[2] > 0:
        operator[2] -= 1
        dfs(total * array[depth], depth + 1)
        operator[2] += 1
    if operator[3] > 0:
        operator[3] -= 1
        dfs(int(total / array[depth]), depth + 1)
        operator[3] += 1

n = int(input())
array = list(map(int, input().split()))
operator = list(map(int, input().split()))
answer = [-inf, inf]

dfs(array[0], 1)

print(*answer, sep='\n')