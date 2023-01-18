num = list(map(int, input().split()))
array = [1, 2, 3, 4, 5]

while num != array:
    for i in range(4):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            print(*num)