num = int(input())

factor = 2

while num != 1:
    if num % factor == 0:
        num = num / factor
        print(factor, end='\n')
    else:
        factor += 1