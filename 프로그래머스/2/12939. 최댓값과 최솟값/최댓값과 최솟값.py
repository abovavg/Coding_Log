def solution(s):
    answer = s.split(' ')
    a = []
    for i in answer:
        a.append(int(i))
        
    m = min(a)
    ma = max(a)
    k = str(m) + ' ' + str(ma)
    return k