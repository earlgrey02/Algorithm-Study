from collections import deque
import sys

input = sys.stdin.readline

def topological_sort():
    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])

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
    costs = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]

    for _ in range(k):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1

    w = int(input())
    dp = [costs[i] if indegree[i] == 0 else 0 for i in range(n + 1)]

    topological_sort()

    print(dp[w])