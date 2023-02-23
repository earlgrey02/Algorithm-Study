def solution(numbers, target):
    def dfs(v, depth):
        if depth == len(numbers):
            if v == target:
                nonlocal answer
                answer += 1
        else:
            dfs(v + numbers[depth], depth + 1)
            dfs(v - numbers[depth], depth + 1)
    
    answer = 0
    dfs(0, 0)

    return answer