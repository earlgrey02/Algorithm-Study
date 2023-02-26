import sys

input = sys.stdin.readline

n = int(input())
times = sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x: (x[1], x[0]))
end = times[0][1]
answer = 1

for time in times[1:]:
    if end <= time[0]:
        answer += 1
        end = time[1]

print(answer)