def solution(myStr):
    answer = []
    li = ['a','b','c']
    if 'a' in myStr and 'b' in myStr and 'c' in myStr:
        for i in li:
            myStr = myStr.replace(i,' ')
        myStr = myStr.split(' ')
        for j in myStr:
            if j != '':
                answer.append(j)
        if len(answer) == 0 :
            answer.append('EMPTY')
    else:
        answer.append('EMPTY')
            
    return answer