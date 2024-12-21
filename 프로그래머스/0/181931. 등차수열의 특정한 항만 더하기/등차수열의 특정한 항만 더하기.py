def solution(a, d, included):
    answer = 0
    aa = len(included)
    for i in range(aa):
        if included[i] == True:
            answer += (d * i) + a
    return answer