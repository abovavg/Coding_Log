def solution(n):
    answer = 0
    for i in range(1,9000000):
        if i**2 == n:
            answer = (i+1)**2
    if answer == 0:
        answer = -1
    return answer