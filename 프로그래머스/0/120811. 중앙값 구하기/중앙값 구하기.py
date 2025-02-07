def solution(array):
    answer = 0
    array = sorted(array)
    if len(array) % 2 == 0:
        answer = (len(array) //2) + ((len(array) // 2) +1) / 2
    else:
        answer = array[len(array) // 2]
    return answer