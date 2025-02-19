def solution(s):
    answer = True
    pc,yc = 0,0
    s = s.lower()
    for i in s:
        if i == 'p':
            pc += 1
        elif i == 'y':
            yc += 1

    if pc == yc and pc == 0 and yc == 0:
        answer = True 
    elif pc != yc :
        answer = False

    return answer