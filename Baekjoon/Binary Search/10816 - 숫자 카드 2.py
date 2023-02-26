from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

_ = int(input())
owns = sorted(list(map(int, input().split())))
_ = int(input())
cards = list(map(int, input().split()))
results = list()

for card in cards:
    results.append(bisect_right(owns, card) - bisect_left(owns, card))

for result in results:
    print(result, end=" ")