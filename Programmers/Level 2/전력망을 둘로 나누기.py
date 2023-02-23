from collections import deque
from itertools import combinations
from math import inf

def solution(n, wires):
    answer = inf

    def bfs(v):
        queue = deque([v])
        visited[v] = True
        cnt = 1
        
        while queue:
            v = queue.popleft()
            cnt += 1
            for next_v in graph[v]:
                if not visited[next_v]:
                    visited[next_v] = True
                    queue.append(next_v)
                    
        return cnt

    for wires in combinations(wires, n - 2):
        graph = {i: [] for i in range(1, n + 1)}
        visited = {i: False for i in range(1, n + 1)}
        cnts = []
    
        for start, end in wires:
            graph[start].append(end)
            graph[end].append(start)

        for i in range(1, n + 1):
            if not visited[i]:
                cnts.append(bfs(i))

        answer = min(answer, abs(cnts[0] - cnts[1]))
    
    return answer