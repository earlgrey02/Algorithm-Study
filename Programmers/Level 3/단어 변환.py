from collections import deque, defaultdict

def solution(begin, target, words):
    visited = defaultdict(int)
    
    def bfs(v):
        queue = deque([v])
        
        while queue:
            v = queue.popleft()
            if v == target:
                return visited[v]
            for word in words:
                if not visited[word] and len(list(filter(lambda x: x[0] != x[1] , zip(v, word)))) == 1:
                    visited[word] = visited[v] + 1
                    queue.append(word)
        
        return 0
    
    return bfs(begin)