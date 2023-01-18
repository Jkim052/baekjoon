t = int(input())

for i in range(t):
    r, sen  = input().split()
    p = str()
    for let in sen:
        for j in range(int(r)):
            p += let
    print(p)