import sys

input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 != v2:
        if rank[v1] == rank[v2]:
            parent[v2] = v1
            rank[v1] += 1
        elif rank[v1] < rank[v2]:
            parent[v1] = v2
        else:
            parent[v2] = v1

n, m = map(int, input().split())
_, *true_people = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]
parties = []
answer = 0

for _ in range(m):
    count, *people = map(int, input().split())
    parties.append(people)
    if count > 1:
        for i in range(count - 1):
            union(people[i], people[i + 1])

true_people = set([find(i) for i in true_people])

for people in parties:
    party = True
    for person in people:
        if find(person) in true_people:
            party = False
            break
    if party:
        answer += 1

print(answer)