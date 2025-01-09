def solution(my_string, is_prefix):
    answer = 0
    re = []
    for i in range(1,len(my_string)+1):
        re.append(my_string[:i])
    if is_prefix in re:
        answer = 1
    else:
        answer = 0
    return answer