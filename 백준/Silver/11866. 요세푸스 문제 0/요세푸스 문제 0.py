from collections import deque

n, k = map(int, input().split())

a = deque(range(1, n + 1))
ans = []

while a:
	for i in range(k):
		a.append(a.popleft())
	ans.append(a.pop())

print('<', end='')
print(*ans, sep=", ", end='')
print('>')