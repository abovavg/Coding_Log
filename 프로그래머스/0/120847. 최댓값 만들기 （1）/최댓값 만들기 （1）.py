def solution(numbers):
    answer = 0
    mf,bmf = 0,1
    a = max(numbers)
    k = numbers.index(max(numbers))
    for i in numbers:
        if bmf < i and numbers.index(i) != k:
            mf = i
            bmf = mf
    answer = bmf * a
    return answer