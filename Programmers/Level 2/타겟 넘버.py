def solution(numbers, target):
    answer = 0
    
    def dfs(v, depth):
        if depth == len(numbers):
            if v == target:
                nonlocal answer
                answer += 1
        else:
            dfs(v + numbers[depth], depth + 1)
            dfs(v - numbers[depth], depth + 1)
            
    dfs(0, 0)
    
    return answer