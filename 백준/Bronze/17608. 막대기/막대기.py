import sys

n = int(sys.stdin.readline())

pillar = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0

height = 0

for i in range(n):
    if i == 0:
        cnt = 1
        height = pillar.pop()
    else:
        cur = pillar.pop()
        if height < cur:
            height = cur
            cnt += 1

print(cnt)