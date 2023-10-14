import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
poke_dict = {}

for i in range(n):
	poke_dict[input().rstrip()] = i + 1

num_poke_dict = {v : k for k, v in poke_dict.items()}

for i in range(m):
	quiz = input().rstrip()
	if ord(quiz[0]) >= 65:
		print(poke_dict[quiz])
	else:
		print(num_poke_dict[int(quiz)])