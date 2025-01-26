def solution(n):
    answer = []
    for i in range(n):
        k = []
        for j in range(n):
            if i == j:
                k.append(1)
            else:
                k.append(0)
        answer.append(k)
    return answer