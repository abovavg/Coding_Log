def solution(strArr):
    answer = 0
    a = [0]*30
    for i in strArr:
        for j in range(0,30):
            if len(i) == j+1:
                a[j] += 1
    answer = max(a)
    return answer