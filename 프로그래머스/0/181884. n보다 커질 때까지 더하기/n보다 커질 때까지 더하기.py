def solution(numbers, n):
    answer = 0
    result = 0
    for i in numbers:
        answer += i
        if answer > n:
            result = answer
            break
            
    return result