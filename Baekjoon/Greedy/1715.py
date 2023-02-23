import heapq
import sys

input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
answer = 0

while len(cards) > 1:
    temp = sum([heapq.heappop(cards) for _ in range(2)])
    heapq.heappush(cards, temp)
    answer += temp

print(answer)