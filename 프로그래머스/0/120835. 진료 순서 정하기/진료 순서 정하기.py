def solution(emergency):
    answer = emergency.copy()
    e = []
    bm = 0
    for j in range(1, len(emergency)+1):
        k = 1
        for i in emergency:
            if k < i and i not in e:
                bm = i
                k = bm
                
                
        a = emergency.index(k)
        e.append(k)
        answer[a] =j
    return answer