def solution(num_list):
    answer = 0
    s = True
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            s = False
            break
    if s == True:
        answer = -1
    return answer