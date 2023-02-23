import sys

input = sys.stdin.readline

n = int(input())
dp = [[0, 0] for i in range(3)]
temp = [[0, 0] for _ in range(3)]

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            temp[j] = [i + a for i in [max(dp[j][0], dp[j + 1][0]), min(dp[j][1], dp[j + 1][1])]]
        elif j == 2:
            temp[j] = [i + c for i in [max(dp[j][0], dp[j - 1][0]), min(dp[j][1], dp[j - 1][1])]]
        else:
            temp[j] = [i + b for i in [max(dp[j][0], dp[j - 1][0], dp[j + 1][0]), min(dp[j][1], dp[j - 1][1], dp[j + 1][1])]]
    for j in range(3):
        dp[j] = temp[j]

print(max(map(lambda x: x[0], dp)), min(map(lambda x: x[1], dp)))