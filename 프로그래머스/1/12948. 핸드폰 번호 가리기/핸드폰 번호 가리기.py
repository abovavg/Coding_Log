def solution(phone_number):
    a = phone_number[:-4]
    aa = len(a)
    answer = ''
    for i in a:
        answer += '*'
    answer += phone_number[aa:]
    return answer