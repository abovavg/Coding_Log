def solution(babbling):
    answer = 0
    ong = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for j in range(len(ong)):
            babbling[i] = babbling[i].replace(ong[j],'/')
    
    for k in babbling:
        if k == '/' or k == '//' or k == '///' or k== '////':
            answer += 1

    return answer