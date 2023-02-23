from itertools import permutations

def solution(k, dungeons):
    answers = []
    for i in permutations(dungeons, len(dungeons)):
        temp = 0
        temp_k = k
        for dungeon in i:
            if dungeon[0] <= temp_k:
                temp_k -= dungeon[1]
                temp += 1
        answers.append(temp)

    return max(answers)