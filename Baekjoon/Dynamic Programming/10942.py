import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
m = int(input())

for i in range(n - 1):
    if array[i] == array[i + 1]:
        dp[i][i + 1] = 1

for length in range(2, n):
    for start in range(n - length):
        end = start + length
        if dp[start + 1][end - 1] and array[start] == array[end]:
            dp[start][end] = 1

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start - 1][end - 1])