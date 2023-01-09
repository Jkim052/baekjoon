num = []
f = []
for i in range(0, 28):
    num.append(int(input()))

for i in range(1, 31):
    if i not in num:
        f.append(i)
print(min(f))
print(max(f))