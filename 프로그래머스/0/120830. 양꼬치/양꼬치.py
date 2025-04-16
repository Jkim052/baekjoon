def solution(n, k):
    num = n // 10
    
    serv = k - num

    answer = n * 12000 + serv * 2000
    return answer