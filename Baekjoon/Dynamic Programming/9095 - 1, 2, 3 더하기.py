import sys

input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]
dp = [0 for _ in range(11)]
dp[1:4] = [1, 2, 4]

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(*[dp[i] for i in nums], sep="\n")