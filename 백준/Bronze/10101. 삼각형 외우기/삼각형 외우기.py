angle = []

for i in range(3):
    angle.append(int(input()))


tri = set(angle)

if sum(angle) != 180:
    print('Error')
else:
    if len(tri) == 3:
        print('Scalene')
    if len(tri) == 2:
        print('Isosceles')
    if len(tri) == 1:
        print('Equilateral')