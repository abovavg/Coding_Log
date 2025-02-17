def solution(str_list):
    answer = []
    if 'l' in str_list and 'r' in str_list:
        
        if str_list.index('l') < str_list.index('r'):
            for i in range(str_list.index('l')):
                answer.append(str_list[i])
        else:
            for i in range(str_list.index('r')+1,len(str_list)):
                answer.append(str_list[i])
    elif 'l' in str_list and 'r' not in str_list:
        for i in range(str_list.index('l')):
            answer.append(str_list[i])
    elif 'l' not in str_list and 'r' in str_list:
        for i in range(str_list.index('r')+1,len(str_list)):
            answer.append(str_list[i])
    else:
        answer = []
    return answer