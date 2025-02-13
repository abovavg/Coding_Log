def solution(before, after):
    answer = 0
    for i in before:
        if before.count(i) != after.count(i):
            answer = 0
            break
        else:
            answer = 1
    return answer