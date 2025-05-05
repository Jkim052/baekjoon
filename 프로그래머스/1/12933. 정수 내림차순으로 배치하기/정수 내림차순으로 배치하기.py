def solution(n):
    answer = 0
    a = []
    while(n > 0):
        a.append(n % 10)
        n = n // 10
        
    a.sort(reverse=True)
    for i in a:
        answer *= 10
        answer += i
    print(a)
    return answer