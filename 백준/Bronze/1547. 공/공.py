m = int(input())

cup = 1

for i in range(m):
    a, b = map(int, input().split())
    if cup in [a,b]:
        if cup == a:
            cup = b
        else:
            cup = a
    else: pass

print(cup)