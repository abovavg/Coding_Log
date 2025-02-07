def solution(n):
    answer = 0
    k,c= 0,1
    for i in range(1,3628800):
        if c > n:
            answer = k-1
            break
        else:
            k += 1
            c *= k
    return answer