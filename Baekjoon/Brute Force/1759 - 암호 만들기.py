from collections import deque
import sys

input = sys.stdin.readline

def dfs(pw, depth):
    if depth == l:
        co_cnt = 0
        vo_cnt = 0
        for i in range(l):
            if pw[i] in ('a', 'e', 'i', 'o', 'u'):
                vo_cnt += 1
            else:
                co_cnt += 1
        if co_cnt >= 2 and vo_cnt >= 1:
            print(pw)
        return
    
    for char in chars:
        if not pw or (ord(pw[-1]) < ord(char) and not visited[char]):
            visited[char] = True
            dfs(pw + char, depth + 1)
            visited[char] = False

l, c = map(int, input().split())
chars = sorted(input().split())
visited = {char: False for char in chars}

dfs("", 0)