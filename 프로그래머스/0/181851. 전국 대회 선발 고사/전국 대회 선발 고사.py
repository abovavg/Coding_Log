def solution(rank, attendance):
    answer = 0
    li = []
    for i in range(1,len(rank)+1):
        ind = rank.index(i)
        if attendance[ind] == True:
            li.append(ind)
        elif len(li) == 3:
            break
    answer = 10000 * li[0] + 100 * li[1] + li[2]
    return answer