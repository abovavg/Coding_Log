def solution(str1, str2):
    answer = 0
    
    a = str1.replace(str2,' ')
    if ' ' in a:
        answer = 1
    else:
        answer =2
    return answer
