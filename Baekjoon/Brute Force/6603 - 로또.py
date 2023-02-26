import sys

input = sys.stdin.readline

def dfs(lotto):
    if len(lotto) == 6:
        print(*lotto)
        return
    
    for i in nums:
        if not lotto or (lotto[-1] < i and i not in lotto):
            dfs(lotto + [i])

while True:
    string = input().strip()
    if string == '0':
        break
    k, *nums = map(int, string.split())

    dfs([], )

    print()