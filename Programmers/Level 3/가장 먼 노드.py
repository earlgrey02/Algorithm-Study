from collections import deque

def solution(n, edge):
    def bfs(v):
        queue = deque([v])
        visited[v] = 1

        while queue:
            v = queue.popleft()
            for next_v in graph[v]:
                if not visited[next_v]:
                    visited[next_v] = visited[v] + 1
                    queue.append(next_v)
        
    graph = {i: [] for i in range(1, n + 1)}
    visited = {i: 0 for i in range(1, n + 1)}
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    bfs(1)

    return len(list(filter(lambda x: x == max(visited.values()), visited.values())))