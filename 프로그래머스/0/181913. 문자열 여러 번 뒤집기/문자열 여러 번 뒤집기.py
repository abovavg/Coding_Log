def solution(my_string, queries):
    answer = ''
    temp = my_string
    for i in queries:
        temp = list(temp)
        temp[i[0]:i[1]+1] = temp[i[0]:i[1]+1][::-1]
        temp = ''.join(temp)
    return temp