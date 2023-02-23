from collections import defaultdict
from copy import deepcopy

def solution(tickets):
    def dfs(v):
        nonlocal answer

        if len(visited) == len(tickets) + 1:
            answer = deepcopy(visited)
            return
        elif answer:
            return

        for next_v in graph[v]:
            graph[v].remove(next_v)
            visited.append(next_v)
            dfs(next_v)
            graph[v].append(visited.pop())
            graph[v].sort()
            
    graph = defaultdict(list)
    answer = []
    visited = ["ICN"]
    
    for start, end in tickets:
        graph[start].append(end)
        
    for key in graph.keys():
        graph[key].sort()

    dfs("ICN")

    return answer