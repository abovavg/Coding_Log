def solution(array, n):
    answer = 0
    mm = 100

    for i in array:
        a = abs(n - i)
        if mm > a:
            mm = a
            answer = i
        elif mm == a:
            if answer > i:
                answer = i
    

    return answer