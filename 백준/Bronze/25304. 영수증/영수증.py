X = int(input())
t = int(input())
s = 0

for _ in range(t):  # t 만큼 반복
    a,b = map(int,input().split())
    s += a*b

if s == X:
    print("Yes")
else:
    print("No")