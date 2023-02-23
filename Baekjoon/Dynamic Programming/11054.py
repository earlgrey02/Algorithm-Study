import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
increase_dp = [1 for _ in range(n)]
decrease_dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if array[j] < array[i]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

print(max([increase_dp[i] + decrease_dp[i] - 1 for i in range(n)]))