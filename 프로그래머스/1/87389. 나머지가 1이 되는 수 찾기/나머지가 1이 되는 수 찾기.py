def solution(n):
    answer = 0
    m = 999997
    for i in range(1,n+1):
        if n % i == 1:
            if m > i:
                m = i
                answer = m
    return answer