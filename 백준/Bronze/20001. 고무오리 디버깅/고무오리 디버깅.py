c = input()
problem = []

while True:
    word = input()
    
    if word == '고무오리 디버깅 끝':
        break

    else:  
        if word == '문제':
            problem.append(word)
        else:
            if len(problem) == 0:
                problem.append('문제')
                problem.append('문제')
            
            else:
                problem.pop()

if len(problem) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')