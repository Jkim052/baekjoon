from collections import deque
import sys

que = deque()
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
	order = input().rstrip()
	if order[0:4] == 'push':
		que.appendleft(int(order[5:]))
	elif order[0:3] == 'pop':
		try:
			print(que.pop())
		except:
			print(-1)
	elif order[0:4] == 'size':
		print(len(que))
	elif order[0:5] == 'empty':
		if len(que) == 0:
			print(1)
		else:
			print(0)
	elif order[0:5] == 'front':
		try:
			print(que[-1])
		except:
			print(-1)
	else:
		try:
			print(que[0])
		except:
			print(-1)