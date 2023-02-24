import sys

input = sys.stdin.readline

str_1, str_2 = [input().strip() for _ in range(2)]
dp = [[0 for _ in range(len(str_2) + 1)] for _ in range(len(str_1) + 1)]

for i in range(1, len(str_1) + 1):
    for j in range(1, len(str_2) + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])