def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        answer.append(arr[i])
        if arr[i] == arr[i-1]:
            answer.pop()
        else:
            pass
    return answer