square = [list(map(int, input().split())) for _ in range(4)]

max_value = max(map(max, square))

grid = [[0]*max_value for _ in range(max_value)]


for i in range(4):
    if square[i][0] > square[i][2]:
        a = square[i][0]
        b = square[i][2]
    else: 
        a = square[i][2]
        b = square[i][0]
    if square[i][1] > square[i][3]:
        c = square[i][1]
        d = square[i][3]
    else:
        c = square[i][3]
        d = square[i][1]

        for j in range(b, a):
            for k in range(d, c):
                grid[j][k] = 1

print(sum(map(sum, grid)))