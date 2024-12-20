def solution(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)) or int(str(a) + str(b)) == int(str(b) + str(a)):
        answer = int(str(a)+str(b))
    elif int(str(b) + str(a)) > int(str(a) + str(b)):
        answer = int(str(b) + str(a))


    return answer