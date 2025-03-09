
def solution(n):
    answer,a = 0,0
    for j in range(1,n):
        a = 0
        for i in range(j,n+1):
            a += i
            if a == n:
                answer +=1
                break
            if a > n:
                break
    return answer+1