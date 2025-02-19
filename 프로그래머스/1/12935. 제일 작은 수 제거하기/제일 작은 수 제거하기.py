def solution(arr):
    answer = []
    a = 9999
    for i in arr:
        if a >= i:
            a = i
    arr.remove(a)
    if len(arr) == 0:
        arr.append(-1)
    return arr