def solution(id_pw, db):
    answer = ''
    a = []
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            a.append('login')
        elif id_pw[1] == i[1] :
            a.append('fail')
        elif id_pw[0] :
            a.append('wrong pw')
    if 'login' in a:
        answer = 'login'
    else:
        answer = a[0]
    
    return answer