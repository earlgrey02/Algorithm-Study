import sys

input = sys.stdin.readline

t = int(input())

dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(3, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])