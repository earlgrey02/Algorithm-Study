from itertools import permutations
from math import sqrt

def solution(numbers):
    array = []

    for i in range(len(numbers)):
        array.extend(list(permutations(numbers, i + 1)))

    numbers = set(map(lambda x: int("".join(x).strip()), array))
    n = max(numbers)
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    
    return len(list(filter(lambda x: primes[x], numbers)))