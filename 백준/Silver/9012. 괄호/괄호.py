t = int(input())

for i in range(t):
    ps = input()

    while True:
        pst = ps
        ps = ps.replace('()', '')
        if pst == ps:break
    
    if len(ps) == 0:
        print('YES')
    else:
        print('NO')