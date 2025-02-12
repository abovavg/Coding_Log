def solution(array):
    answer = 0
    k = 0
    d = 0
    for i in array:
        if answer < array.count(i) or i == k:
            answer = array.count(i)
            k = i
        elif answer == array.count(i):
            k = -1
    return k