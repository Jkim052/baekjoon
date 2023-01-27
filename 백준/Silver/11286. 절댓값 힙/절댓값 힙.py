import heapq
import sys
t = int(sys.stdin.readline().rstrip())

plus = []


for i in range(t):

    n = int(sys.stdin.readline().rstrip())

    if n != 0:
        heapq.heappush(plus, (abs(n), n))
    else:
        if plus:
            print(heapq.heappop(plus)[1])
        else:
            print(0)