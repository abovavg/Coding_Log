def solution(order):
    answer = 0
    for i in order:
        if 'ameri' in i:
            answer += 4500
        elif 'latte' in i:
            answer += 5000
        elif 'anything' in i:
            answer += 4500
                
    return answer