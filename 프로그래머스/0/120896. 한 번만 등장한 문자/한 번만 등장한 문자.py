def solution(s):
    answer = ''
    re = []
    a = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    for i in answer:
        re.append(i)
    re = sorted(re)
    for i in re:
        a += i
    return a