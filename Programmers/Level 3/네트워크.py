from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def bfs(v):
        queue = deque([v])
        visited[v] = True
        
        while queue:
            v = queue.popleft()
            for i, _ in filter(lambda x: x[1], enumerate(computers[v])):
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)
    
    return answer