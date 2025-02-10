def solution(age):
    answer = ''
    real = ''
    al = 'abcdefghijklmnopqrspuvwuxyz'
    for j in str(age):
        real += al[int(j)]
    return real