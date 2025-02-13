def solution(array):
    answer = 0
    for i in str(array):
        for j in i:
            if j == '7':
                answer +=1
    return answer