def solution(polynomial):
    answer = ''
    p = polynomial.split(' ')
    a,b,c = 0,0,0
    for i in p:
        if i.isnumeric() == True:
            a += int(i)
        elif i == 'x':
            c += 1
        elif i != '+':
            j = i.replace('x','')
            b += int(j)

    if a == 0:
        if str(b+c) == str(1):
            answer = 'x'
        else:
            answer = str(b+c)+'x'
    else:
        if b+c == 0:
            answer = str(a)
        elif str(b+c) == str(1):
            answer = 'x + ' + str(a)
        else:
            answer = str(b+c)+'x + '+ str(a)
    return answer