from math import inf
import sys

input = sys.stdin.readline

def dfs(array):
    global answer

    if len(array) == n:
        answer = max(answer, sum([abs(nums[array[i]] - nums[array[i + 1]]) for i in range(n - 1)]))
        return

    for i in range(n):
        if i not in array:
            dfs(array + [i])

n = int(input())
nums = list(map(int, input().split()))
answer = -inf

dfs([])

print(answer)