import sys

while True:
	sentence = sys.stdin.readline().rstrip()
	stack = []
	x = True
	if sentence == '.':
		break
	for i in sentence:
		if (i == "(" or i == "["):
			stack.append(i)
		if (i == ")" or i == "]"):
			try:
				a = stack.pop()
			except:
				x = False
				break
			if (a == "(" and i != ")"):
				x = False
				break
			if (a == "[" and i != "]"):
				x = False
				break
	if len(stack) != 0:
		x = False
	if x == True:
		print('yes')
	else:
		print('no')