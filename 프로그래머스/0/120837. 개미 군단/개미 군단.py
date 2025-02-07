def solution(hp):
    answer,a = 0,0
    a = hp // 5
    if hp % 5 == 0:
        answer = a
    elif hp % 5 != 0:
        b = (hp-(5*a)) // 3
        if (hp-(5*a)) % 3 == 0:
            answer = a + b
        else:
            c = hp - ((a*5) + (3*b))
            answer = a + b + c
    return answer