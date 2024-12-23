def solution(l, r):
    a = ['0','5']
    answer = []

    for i in range(l,r+1):
        state = True
        for j in str(i):
            if j not in a:
                state = False
                break
        if state == True:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    
    return answer