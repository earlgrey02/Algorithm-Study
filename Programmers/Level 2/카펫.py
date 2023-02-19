def solution(brown, yellow):
    area = brown + yellow
    
    for i in range(3, area):
        if area % i == 0:
            j = area // i
            if j >= i and (2 * i + 2 * j) == brown + 4:
                answer = [j, i]
                break

    return answer