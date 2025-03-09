def solution(sides):
    answer,r = 0,0
        
    a = max(sides)
    b = sides.index(a)
    for i in range(0,len(sides)):
        if sides[0] == sides[1] and sides[1] == sides[2]:
            answer = 99999
            break
        elif i != b:
            answer += sides[i]

    if a < answer:
        r = 1
    elif a >= answer:
        r = 2
    return r