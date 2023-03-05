from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v][0] = 0
    visited[v][1] = 1

    while queue:
        v = queue.popleft()
        for next_v in (v - 1, v + 1, v * 2):
            if 0 <= next_v <= 100000:
                if visited[next_v][0] == -1:
                    visited[next_v][0] = visited[v][0] + 1
                    visited[next_v][1] = visited[v][1]
                    queue.append(next_v)
                elif visited[next_v][0] == visited[v][0] + 1:
                    visited[next_v][1] += visited[v][1]
                    

n, k = map(int, input().split())
visited = defaultdict(lambda: [-1, 0])

bfs(n)

print(visited[k][0])
print(visited[k][1])