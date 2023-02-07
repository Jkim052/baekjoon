import sys

n = int(sys.stdin.readline())

people_list = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    people_list.append((a, b))

for i in people_list:
    rank = 1
    for j in people_list:
        if ((j[0] > i[0]) and (j[1] > i[1])):
            rank += 1
    print(rank)