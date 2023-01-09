num = []
s1 = set()
for i in range(0, 10):
    num.append(int(input()))

for i in num:
    s1.add(i % 42)

print(len(s1))