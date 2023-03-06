from bisect import bisect_left
from math import inf
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
stack = [-inf]
index = []
answer = []

for i in array:
    if stack[-1] < i:
        index.append((len(stack), i))
        stack.append(i)
    else:
        idx = bisect_left(stack, i)
        stack[idx] = i
        index.append((idx, i))

length = len(stack) - 1

while length and index:
    idx, i = index.pop()
    if idx == length:
        answer.append(i)
        length -= 1

print(len(answer))
print(*answer[::-1])