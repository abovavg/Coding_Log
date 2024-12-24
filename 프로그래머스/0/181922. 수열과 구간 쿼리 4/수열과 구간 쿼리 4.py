def solution(arr, queries):
    answer = []
    for j in queries:
        for i in range(j[0],j[1]+1):
            if i % j[2] == 0:
                arr[i] += 1
    answer =arr    
    return answer