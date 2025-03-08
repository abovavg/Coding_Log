def solution(balls, share):
    answer,a,b,c = 0,1,1,1
    for i in range(1,balls+1):
        a *= i
    for i in range(1,(balls-share)+1):
        b *= i
    for i in range(1,share+1):
        c *= i 
    
    answer = a / (b * c)
    return answer