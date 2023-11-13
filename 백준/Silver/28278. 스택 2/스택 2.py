import sys

input = sys.stdin.readline
n = int(input().rstrip())

stack = []

for i in range(n):
	a = input().rstrip()
	if a[0] == '1':
		stack.append(int(a[2:]))
	if a[0] == '2':
		try:
			print(stack.pop())
		except:
			print(-1)
	if a[0] == '3':
		print(len(stack))
	if a[0] == '4':
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	if a[0] == '5':
		try:
			print(stack[-1])
		except:
			print(-1)