def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        a = i[s:s+l]
        if int(a) > k:
            answer.append(int(a))
        
    return answer