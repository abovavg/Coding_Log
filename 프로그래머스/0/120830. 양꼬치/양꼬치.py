def solution(n, k):
    answer = 0
    if n >=10:
        kk =  n // 10
        answer = 12000 * n + 2000 * k - kk*2000
    else:
        answer = 12000 * n + 2000 * k 
    return answer