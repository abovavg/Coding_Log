def solution(myString):
    answer = []
    myString = myString.split('x')
    for i in myString:
        if i == '':
            answer.append(0)
        else:
            answer.append(len(i))
    return answer