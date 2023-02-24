from bisect import bisect_left
from math import inf
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
stack = [-inf]

for i in array:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i

print(len(stack) - 1)