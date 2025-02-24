def solution(num):
    answer = 0
    n = num
    for i in range(8000000):
        if n != 1:
            if n % 2 == 0:
                n = n //2
                answer += 1
            elif n % 2 == 1:
                n = n*3 + 1
                answer += 1
 
        else:
            break        
    if num == 1:
        answer = 0
    elif answer > 500:
        answer = -1
    return answer