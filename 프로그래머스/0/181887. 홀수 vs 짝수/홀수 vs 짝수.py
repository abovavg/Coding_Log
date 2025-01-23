def solution(num_list):
    answer = 0
    p,m = 0,0
    for i in range(len(num_list)):
        if i % 2 == 0:
            p += num_list[i]
        else:
            m += num_list[i]
    if p >= m:
        answer = p
    else:
        answer = m
    return answer