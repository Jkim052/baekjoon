a = input()

x = len(a)
ans = set()
length = 1
while length < x + 1:
	index = 0
	while (index + length) < x + 1:
		ans.add(a[index: (index + length)])
		index += 1
	length += 1

print(len(ans))