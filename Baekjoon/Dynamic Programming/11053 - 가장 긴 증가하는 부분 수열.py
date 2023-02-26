import sys

input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(1, i):
        if array[j] < array[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))