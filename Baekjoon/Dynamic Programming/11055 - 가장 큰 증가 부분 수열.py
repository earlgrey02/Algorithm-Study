import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [i for i in array]

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))