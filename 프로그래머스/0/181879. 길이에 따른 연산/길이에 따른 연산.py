def solution(num_list):
    b = 1
    a = 0
    answer = 0
    if len(num_list) >= 11:
        for i in num_list:
            a += i
        answer = a
    else:
        for i in num_list:
            b *= i
        answer = b
    return answer