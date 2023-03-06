from math import sqrt
import sys

input = sys.stdin.readline

n = int(input())
primes = [True for _ in range(n + 1)]
primes[0:2] = [False for _ in range(2)]
left, right = 0, 0
sum = 0
answer = 0

for i in range(2, int(sqrt(n)) + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False

primes = list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(primes))))

while True:
    if sum == n:
        answer += 1
    if sum < n:
        if right >= len(primes):
            break
        sum += primes[right]
        right += 1
    else:
        if left >= len(primes):
            break
        sum -= primes[left]
        left += 1

print(answer)