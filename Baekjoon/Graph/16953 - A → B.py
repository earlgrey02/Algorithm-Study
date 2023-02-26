from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        if v == b:
            return visited[v]
        for next_v in (v * 2, int(str(v) + '1')):
            if a < next_v <= b and not visited[next_v]:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return -1

a, b = map(int, input().split())
visited = defaultdict(int)

print(bfs(a))