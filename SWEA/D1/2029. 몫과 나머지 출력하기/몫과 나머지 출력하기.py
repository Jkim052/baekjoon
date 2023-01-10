T = int(input())

for num in range(1, T+1):
        a, b = list(map(int,input().split()))
        s = a // b
        r = a % b
        print(f'#{num} {s} {r}')