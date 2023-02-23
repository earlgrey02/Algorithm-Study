import sys

input = sys.stdin.readline

n, m = map(int, input().split())
v = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
turn = [3, 0, 1, 2]
answer = 0

while True:
    back = True
    if matrix[v[0]][v[1]] == 0:
        answer += 1
        matrix[v[0]][v[1]] = -1

    for i in range(4):
        if matrix[v[0] + dy[i]][v[1] + dx[i]] == 0:
            back = False
            break

    if back:
        if v[2] >= 2:
            i = v[2] - 2
        else:
            i = v[2] + 2
        if matrix[v[0] + dy[i]][v[1] + dx[i]] == 1:
            break
        v[:2] = (v[0] + dy[i], v[1] + dx[i])
    else:
        v[2] = turn[v[2]]
        if matrix[v[0] + dy[v[2]]][v[1] + dx[v[2]]] == 0:
            v = [v[0] + dy[v[2]], v[1] + dx[v[2]], v[2]]

print(answer)