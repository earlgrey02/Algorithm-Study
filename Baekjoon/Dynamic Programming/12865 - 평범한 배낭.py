import sys

input = sys.stdin.readline

n, k = map(int, input().split())
items = [0] + sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
dp = [0 for _ in range(k + 1)]

for item in items[1:]:
    for i in range(k, 0, -1):
        if i >= item[0]:
            dp[i] = max(dp[i - item[0]] + item[1], dp[i])

print(dp[k])