def solution(num, k):
    answer = 0
    for i in str(num):
        if i == str(k):
            answer = int(str(num).index(str(k)))+1
            break
        else:
            answer = -1
    return answer