def solution(arr):
    answer = []
    a,b,bb = 0,0,0
    if 2 not in arr:
        answer.append(-1)
    else:   
        a = arr.index(2)
        b = arr[::-1].index(2)
        bb = len(arr) - b -1
        if a < bb:
            answer = arr[a:bb+1]
        elif a == bb:
            answer.append(arr[a])
    return answer