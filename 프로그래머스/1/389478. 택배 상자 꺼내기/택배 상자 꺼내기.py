def makecago(n, w, num):
    cago = [[0] * w for _ in range((n//w) + 1)]
    box = 0
    for i in range((n//w) + 1):
        for j in range(w):
            box = box + 1
            cago[i][j] = box
            if (box == n):
                return cago
            
def solution(n, w, num):
    x = 0
    y = 0
    
    cago = makecago(n, w, num)
    
            
    for i in range(1, (n//w) + 1, 2):
        cago[i].reverse()
    
    for i in range((n//w) + 1):
        for j in range(w):
               if (cago[i][j] == num):
                    x = j
                    y = i
                    break
    print(cago)
                    
    answer = 0
    for i in range(y, (n//w) + 1):
        if (cago[i][x] != 0):
            answer = answer + 1
    
    return answer
