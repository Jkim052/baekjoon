numlist = []

for i in range(5):
	numlist.append(int(input()))

numlist.sort()
numsum = sum(numlist)

print(int(numsum/5))
print(numlist[2])