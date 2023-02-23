from itertools import combinations
from math import inf
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
houses = [(i, j) for i in range(n) for j in range(n) if matrix[i][j] == 1]
answers = []

for chickens in combinations([(i, j) for i in range(n) for j in range(n) if matrix[i][j] == 2], m):
    total_distance = 0

    for house in houses:
        distance = inf
        for chicken in chickens:
            distance = min(distance, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
        total_distance += distance

    answers.append(total_distance)

print(min(answers))