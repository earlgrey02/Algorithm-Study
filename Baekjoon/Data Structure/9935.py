import sys

input = sys.stdin.readline

string = input().strip()
explosion = input().strip()
size = len(explosion)
stack = []

for i in string:
    stack.append(i)
    if ''.join(stack[-size:]) == explosion:
        for _ in range(size):
            stack.pop()

print(''.join(stack) if len(stack) != 0 else "FRULA")