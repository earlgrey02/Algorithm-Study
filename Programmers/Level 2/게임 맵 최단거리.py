from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    def bfs(v):
        queue = deque([v])
        visited[v[0]][v[1]] = 1

        while queue:
            v = queue.popleft()
            for i in range(4):
                next_v = (v[0] + dy[i], v[1] + dx[i])
                if 0 <= next_v[0] < n and 0 <= next_v[1] < m and maps[next_v[0]][next_v[1]] and not visited[next_v[0]][next_v[1]]:
                    visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                    queue.append(next_v)

    bfs((0, 0))
    
    return visited[n - 1][m - 1] if visited[n - 1][m - 1] else -1