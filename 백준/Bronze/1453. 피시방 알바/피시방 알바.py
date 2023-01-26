n = int(input())
sit = list(map(int, input().split()))

b = set(sit)

print(len(sit) - len(b))