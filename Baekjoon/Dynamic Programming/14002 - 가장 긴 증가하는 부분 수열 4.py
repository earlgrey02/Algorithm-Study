import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [[i] for i in array]

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [array[i]]

length = max(map(lambda x: len(x), dp))

print(length)
print(*list(filter(lambda x: len(x) == length, dp))[0])