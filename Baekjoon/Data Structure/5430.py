from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    array = deque(input().strip()[1:-1].split(','))
    if n == 0:
        array = deque()    
    error = False
    reverse = 0

    for func in p:
        if func == 'R':
            reverse += 1
        else:
            if len(array) == 0:
                error = True
                break
            if reverse % 2 == 0:
                array.popleft()
            else:
                array.pop()

    if error:
        print("error")
    else:
        if reverse % 2 != 0:
            array.reverse()
        print(f"[{','.join(array)}]")