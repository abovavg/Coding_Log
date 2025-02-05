def solution(my_string):
    answer = ''
    i = ['a','i','o','u','e']
    for j in i:
        my_string = my_string.replace(j,'')
    answer = my_string
    return answer