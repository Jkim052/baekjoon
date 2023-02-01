import sys
input = sys.stdin.readline()

a, b = map(str, input.split())

a = list(map(int, list(a)))
b = list(map(int, list(b)))

total = 0

for i in b:
    total += sum(a)*i

print(total)