def solution(arr):
    answer = [[]]
    
    if len(arr) > len(arr[0]):
        a = len(arr) - len(arr[0])
        for i in range(len(arr)):
            for k in range(a):
                arr[i].append(0)
        answer = arr
    elif len(arr) < len(arr[0]):
        a = len(arr[0]) - len(arr)
        for k in range(a):
            arr.append([0]*len(arr[0]))
        answer = arr
    else:
        answer = arr
    return answer