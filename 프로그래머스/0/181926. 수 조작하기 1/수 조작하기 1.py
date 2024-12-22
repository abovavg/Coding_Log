def solution(n, control):
    kk = n
    for i in control:
        if i == 'w':
            kk += 1
        elif i == 's':
            kk -= 1
        elif i == 'd':
            kk += 10
        elif i == 'a':
            kk -= 10
    answer = kk
    return answer