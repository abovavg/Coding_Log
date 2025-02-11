def solution(spell, dic):
    r = []
    re = 0
    for j in dic:
        answer = 0
        for i in range(len(spell)):
            if j.count(spell[i]) == 1:
                answer +=1
            else:
                break
        if answer == len(spell):
            r.append(1)
        else:
            r.append(2)
    if 1 in r:
        re = 1
    else:
        re =2
    return re