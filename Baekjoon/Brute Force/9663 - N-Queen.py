import sys

input = sys.stdin.readline

n = int(input())
row = [0 for _ in range(n)]
visited = [False for _ in range(n)] 
answer = 0

def check(depth):
    for i in range(depth):
        if row[depth] == row[i] or abs(row[i] - row[depth]) == depth - i:
            return False
    return True

def dfs(depth):
    global answer

    if depth == n:
        answer += 1
        return
    for i in range(n):
        if not visited[i]:
            row[depth] = i
            if check(depth):
                visited[i] = True
                dfs(depth + 1)
                visited[i] = False

dfs(0)

print(answer)