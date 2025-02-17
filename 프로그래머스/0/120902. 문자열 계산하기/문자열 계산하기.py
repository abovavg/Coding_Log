def solution(my_string):
    
    my = my_string.split(' ')
    answer = int(my[0])
    for i in range(1,len(my),2):
        if my[i] == '+':
            answer +=int(my[i+1])
        else:
            answer -= int(my[i+1])
    return answer