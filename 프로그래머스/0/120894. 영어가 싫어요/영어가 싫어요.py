def solution(numbers):
    answer = 0
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        if n[i] not in numbers:
            pass
        else:
            numbers = numbers.replace(n[i],str(i))
    answer = int(numbers)
    return answer