import sys

input = sys.stdin.readline

str_1 = " " + input().strip()
str_2 = " " + input().strip()
dp = [[0 for _ in range(len(str_2))] for _ in range(len(str_1))]

for i in range(1, len(str_1)):
    for j in range(1, len(str_2)):
        if str_1[i] == str_2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])