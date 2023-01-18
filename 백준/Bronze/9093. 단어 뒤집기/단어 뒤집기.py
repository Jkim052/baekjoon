t = int(input())

for i in range(t):
    sen = list(input().split())
    new_sen = []
    for j in sen:
        new_sen.append((j[-1 : -(len(j)+1) : -1]))

    print(*new_sen)