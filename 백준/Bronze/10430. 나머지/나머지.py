A,B,C= map(int, input().split())
n1 = (A+B)%C
n2 = ((A%C) + (B%C))%C
n3 = (A*B)%C
n4 = ((A%C) * (B%C))%C

print(n1)
print(n2)
print(n3)
print(n4)