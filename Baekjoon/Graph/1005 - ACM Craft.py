from collections import deque
import sys

input = sys.stdin.readline

def topological_sort():
    queue = deque(list(map(lambda x: x[0], filter(lambda x: x[1] == 0, indegree.items()))))

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            indegree[next_v] -= 1
            dp[next_v] = max(dp[v] + costs[next_v], dp[next_v])
            if indegree[next_v] == 0:
                queue.append(next_v)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    costs = {i + 1: j for i, j in enumerate(map(int, input().split()))}
    graph = {i: [] for i in range(1, n + 1)}
    indegree = {i: 0 for i in range(1, n + 1)}

    for _ in range(k):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1

    w = int(input())
    dp = [0] + [0 if indegree[i] != 0 else costs[i] for i in range(1, n + 1)]

    topological_sort()

    print(dp[w])