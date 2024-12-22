def solution(num_list):
    h = ''
    ch = ''
    for i in num_list:
        if i % 2 == 0:
            ch += str(i)
        else:
            h += str(i)
    answer = int(ch)+int(h)
    return answer