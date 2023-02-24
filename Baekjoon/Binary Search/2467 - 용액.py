from math import inf
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

start, end = 0, n - 1
answer = []
temp = inf

while start < end:
    p = array[start] + array[end]

    if p == 0:
        answer = [array[start], array[end]]
        break
    elif abs(p) < temp:
        answer = [array[start], array[end]]
        temp = abs(p)
    
    if p > 0:
        end -= 1
    else:
        start += 1

print(*answer)