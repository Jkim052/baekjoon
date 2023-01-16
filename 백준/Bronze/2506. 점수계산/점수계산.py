N = int(input())

A = list(map(int, input().split()))

S = 0

score = 0

for i in A:
    if i == 1:
        score += 1
        S += score
    else:
        score = 0

print(S)