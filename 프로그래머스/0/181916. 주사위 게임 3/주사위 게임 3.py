def solution(a, b, c, d):
    answer = 0
    if a == b and b == c and c == d:
        answer = 1111 * a
    elif a == b and b == c and c != d:
        answer = (10 * c + d)**2
    elif b == c and c == d and d != a:
        answer = (10 * d + a)**2
    elif c == d and d == a and a != b:
        answer = (10 * a + b)**2
    elif a == b and b == d and d != c:
        answer = (10 * d+ c)**2
    elif a == b and c == d and a !=c:
        answer = (a + c) * (a - c)
    elif a == c and b == d and a != b:
        answer = (a + b) * (a - b)
    elif b == c and a == d and a != b:
        answer = (a + b) * (a - b)
    elif a == b and c != d:
        answer = c * d
    elif a == c and c != b and b !=d:
        answer = b * d
    elif a == d and d != b and b != c:
        answer = b * c
    elif b == d and d != c and c != a:
        answer = c * a
    elif b == c and c != a and a != d:
        answer = a * d
    elif c == d and d != b and b != a:
        answer = a * b
    elif a != b and b != c and c != d and a != d and a != c and b != d:
        if a < b and a < c and a < d:
            answer = a
        elif b < a and b < c and b < d:
            answer = b
        elif c <a and c < b and c< d:
            answer =c
        else:
            answer = d
    answer = abs(answer)
    return answer