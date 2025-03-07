def solution(arr):
    answer = 0
    a = 0
    for i in range(len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j] == arr[j][i]:
                answer += 1
            elif arr[i][j] != arr[j][i]:
                answer += 0
                break
    if len(arr[0]) * len(arr) == answer:
        a = 1
    else:
        a = 0
    
    return a