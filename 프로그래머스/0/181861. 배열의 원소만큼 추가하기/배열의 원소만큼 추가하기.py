def solution(arr):
    answer = []
    a = ''
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer