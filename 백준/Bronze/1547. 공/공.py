cups = [1, 2, 3]

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    a = cups.index(a)
    b = cups.index(b)
    cups[a], cups[b] = cups[b], cups[a]

print(cups[0])