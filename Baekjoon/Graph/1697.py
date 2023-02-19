from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        for next_v in [v + 1, v - 1, v * 2]:
            if 0 <= next_v <= 100000 and not visited[next_v]:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

n, k = map(int, input().split())
visited = defaultdict(int)

print(bfs(n) - 1)