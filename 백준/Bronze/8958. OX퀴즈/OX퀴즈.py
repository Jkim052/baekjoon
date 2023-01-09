b = int(input())
cnt = 0
total = 0
for i in range(0, b):
    globals()[f"n{str(i)}"]= input()


for j in range(0, b):
    cnt = 0
    total = 0
    for i in globals()[f"n{str(j)}"]: 
        if i == "O":
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)