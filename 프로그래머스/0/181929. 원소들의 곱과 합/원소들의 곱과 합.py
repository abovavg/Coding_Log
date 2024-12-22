def solution(num_list):
    mul = 1
    hap = 0
    for i in num_list:
        mul = mul * i
        hap = hap + i
    hap = hap**2
    
    if mul > hap:
        answer = 0
    else:
        answer = 1
    return answer