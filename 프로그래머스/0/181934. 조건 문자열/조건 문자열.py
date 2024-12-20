def solution(ineq, eq, n, m):
    if ineq == '<' and eq == '=':
        if (n <= m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq == '<' and eq == '!':
        if (n < m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq == '>' and eq == '=':
        if (n >= m) == True:
            answer = 1
        else:
            answer = 0   
    elif ineq == '>' and eq == '!':
        if (n > m) == True:
            answer = 1
        else:
            answer = 0
        
        
    return answer