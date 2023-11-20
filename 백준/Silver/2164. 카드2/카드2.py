from collections import deque

n = int(input())

que = deque(range(1, n + 1))

while True:
	try:
		a = que.popleft()
		que.append(que.popleft())
	except:
		break

print(a)