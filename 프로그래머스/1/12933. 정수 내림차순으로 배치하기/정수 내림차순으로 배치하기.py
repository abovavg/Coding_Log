def solution(n):
    a = ''
    answer = sorted(str(n))[::-1]
    for i in answer:
        a += i
    answer = int(a)
        
    return answer