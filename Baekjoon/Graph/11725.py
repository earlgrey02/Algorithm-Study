from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v, prev):
    answers[v] = prev
    
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = True
            dfs(next_v, v)

n = int(input())
graph = defaultdict(list)
visited = defaultdict(lambda: False)
answers = defaultdict(int)

for _ in range(n - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited[1] = True
dfs(1, 0)

for i in range(2, n + 1):
    print(answers[i])