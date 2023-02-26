from math import comb
import sys

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(comb(m, n))