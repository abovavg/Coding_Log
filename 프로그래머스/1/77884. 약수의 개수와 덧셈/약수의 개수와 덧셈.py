def solution(left, right):
    re = 0
    for i in range(left,right+1):
        answer = 0
        for j in range(1,i+1):
            if i % j == 0:
                answer += 1
        if answer % 2 == 0:
            re += i
        else:
            re -= i
    return re