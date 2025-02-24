def solution(x, n):
    answer = []
    for i in range(1,n+1):
        a = i*x
        if x >= -10000000 and x <=10000000:
            answer.append(a)
            
    return answer