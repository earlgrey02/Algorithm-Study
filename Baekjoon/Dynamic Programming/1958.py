import sys

input = sys.stdin.readline

str_1, str_2, str_3 = [input().strip() for _ in range(3)]
dp = [[[0 for _ in range(len(str_3) + 1)] for _ in range(len(str_2) + 1)] for _ in range(len(str_1) + 1)]

for i in range(1, len(str_1) + 1):
    for j in range(1, len(str_2) + 1):
        for k in range(1, len(str_3) + 1):
            if str_1[i - 1] == str_2[j - 1] == str_3[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k -1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[-1][-1][-1])