passenger =[]

for i in range(4):
    a ,b = map(int, input().split())
    if i == 0:
        passenger.append(b-a)
    else:
        passenger.append((passenger[i-1]+b-a))

if max(passenger) > 10000:
    print(10000)
else:
    print(max(passenger))