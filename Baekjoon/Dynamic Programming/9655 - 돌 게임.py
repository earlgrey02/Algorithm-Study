import sys

input = sys.stdin.readline

n = int(input())
dp = [False for _ in range(n + 1)]
dp[1] = True
if n >= 2:
    dp[2] = False

for i in range(3, n + 1):
    dp[i] = not dp[i - 1]

print("SK" if dp[n] else "CY")