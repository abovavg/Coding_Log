def solution(x):
    answer = True
    som = 0
    for i in str(x):
        som += int(i)
    if x % som == 0:
        answer = True
    else:
        answer = False
    return answer