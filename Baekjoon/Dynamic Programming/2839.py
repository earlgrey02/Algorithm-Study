import sys

input = sys.stdin.readline

n = int(input())
answer = 0

while n > 0:
    if n % 5 == 0:
        answer += n // 5
        break
    n -= 3
    answer += 1

print(answer if n >= 0 else -1)