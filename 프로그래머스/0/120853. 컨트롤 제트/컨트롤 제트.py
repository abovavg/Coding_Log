def solution(s):
    answer = 0
    aa = []
    a = s.split(' ')
    for i,j in enumerate(a):
        if j != 'Z':
            answer += int(j)
            
        elif j == 'Z':
            answer -= int(a[i-1])
        
    return answer