from math import inf
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))
left, right = 0, 0
sum = 0
answer = inf

while True:
    if sum < s:
        if right >= n:
            break
        sum += array[right]
        right += 1
    else:
        if left >= n:
            break
        answer = min(answer, right - left)
        sum -= array[left]
        left += 1

print(answer if answer != inf else 0)