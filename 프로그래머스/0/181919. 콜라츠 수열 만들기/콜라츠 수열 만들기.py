def solution(n):
    answer = []
    count = 0
    answer.append(n)
    while True:
        if n % 2 == 0:
            n = n/2
            answer.append(n)
            count += 1
        elif n == 1:
            break
        else:
            n = 3*n+1
            answer.append(n)
            count += 1
            
    return answer