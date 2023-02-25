import sys

input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [cards[i] for i in range(n + 1)]
answer = 0

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])