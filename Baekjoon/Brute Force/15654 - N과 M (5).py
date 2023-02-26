import sys

input = sys.stdin.readline

def dfs(array):
    if len(array) == m:
        print(*array)
        return
    
    for i in nums:
        if i not in array:
            dfs(array + [i])

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))

dfs([])