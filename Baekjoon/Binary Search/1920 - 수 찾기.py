from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

_ = int(input())
array_1 = sorted(list(map(int, input().split())))
_ = int(input())
array_2 = list(map(int, input().split()))

for i in array_2:
    if bisect_right(array_1, i) - bisect_left(array_1, i):
        print(1)
    else:
        print(0)