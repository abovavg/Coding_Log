def solution(my_string):
    st_r = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b',"c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = [0] *52
    for i in my_string:
        a = st_r.index(i)
        answer[a] += 1
        
    return answer