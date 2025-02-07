def solution(score):
    answer = []
    k = []
    c = []
    for a,b in score:
        result = (a + b) /2
        answer.append(result)
    k = sorted(answer)[::-1]
    for i in range(len(k)):
        c.append(k.index(answer[i])+1)
    return c