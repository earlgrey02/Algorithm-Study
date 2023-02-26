import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    dp[0] = [1, 0]
    if n >= 1:
        dp[1] = [0, 1]

    for i in range(2, n + 1):
        for j in range(2):
            dp[i][j] = dp[i - 2][j] + dp[i - 1][j]
    
    print(*dp[n])