import sys

input = sys.stdin.readline

m = int(input())
s = 0b0

for _ in range(m):
    order = input().strip()

    try: 
        command, n = order.split()
        n = int(n)
        if command == "add": 
            s = s | (0b1 << n)
        elif command == "remove":
            s = s & ~(0b1 << n)
        elif command == "check":
            if s & (0b1 << n):
                print(1)
            else:
                print(0)
        elif command == "toggle":
            s = s ^ (0b1 << n)
    except:
        if order == "all":
            s = 0b111111111111111111111
        elif order == "empty":
            s = 0b0