def solution(number):
    answer = 0
    if int(number) > 0 :
        for i in number:
            answer += int(i)
        answer = answer % 9
    return answer