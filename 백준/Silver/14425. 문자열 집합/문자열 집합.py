n, m = map(int, input().split())
a = {}
for i in range(n):
	a[input()] = 0
for j in range(m):
	x = input()
	if x in a:
		a[x] += 1


print(sum(a.values()))