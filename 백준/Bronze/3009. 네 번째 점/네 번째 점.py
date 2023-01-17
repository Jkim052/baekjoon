length = []
width = []
for i in range(3):
    a, b = map(int, input().split())
    length.append(a)
    width.append(b)

for l in length:
    if length.count(l) ==1:
        print(l)


for w in width:
    if width.count(w) ==1:
        print(w)
       