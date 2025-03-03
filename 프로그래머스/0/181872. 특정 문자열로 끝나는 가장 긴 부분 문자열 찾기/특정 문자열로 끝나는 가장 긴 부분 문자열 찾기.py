def solution(myString, pat):
    answer = ''
    a,b = 0,0
    if len(pat) == 1:
        a = myString.index(pat[0])
    else:
        a = myString.index(pat[-1])
    for i in myString:
        if i == myString[a]:
            b = myString.rfind(i)
    answer = myString[:b+1]
    return answer