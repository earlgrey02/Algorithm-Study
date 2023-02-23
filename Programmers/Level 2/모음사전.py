from itertools import product

def solution(word):
    words = []

    for i in range(1, 6):
        words.extend(map("".join, product(['A', 'E', 'I', 'O', 'U'], repeat=i)))

    return sorted(words).index(word) + 1