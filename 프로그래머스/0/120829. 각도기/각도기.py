def solution(angle):
    answer = 0
    if angle == 180:
        answer = 4
    elif angle <180 and angle > 90:
        answer = 3
    elif angle == 90:
        answer = 2
    else:
        answer = 1
    return answer