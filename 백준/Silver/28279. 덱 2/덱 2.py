from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())
deq = deque()
for i in range(n):
	a = input().rstrip()
	if a[0:1] == "1":
		deq.appendleft(int(a[2:]))
	elif a[0:1] == "2":
		deq.append(int(a[2:]))
	elif a[0:1] == "3":
		try:
			print(deq.popleft())
		except:
			print(-1)
	elif a[0:1] == "4":
		try:
			print(deq.pop())
		except:
			print(-1)
	elif a[0:1] == "5":
		print(len(deq))
	elif a[0:1] == "6":
		if deq:
			print(0)
		else:
			print(1)
	elif a[0:1] == "7":
		try:
			print(deq[0])
		except:
			print(-1)
	else:
		try:
			print(deq[-1])
		except:
			print(-1)