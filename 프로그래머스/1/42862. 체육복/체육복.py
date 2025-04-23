def solution(n, lost, reserve):
    real_lost = sorted(set(lost) - set(reserve))
    real_reserve = sorted(set(reserve) - set(lost))
    
    for j in real_reserve:
        if (j - 1 in real_lost):
            real_lost.remove(j - 1)
        elif (j + 1 in real_lost):
            real_lost.remove(j + 1)
            
    answer = n - len(real_lost)
    return answer


    