x = input()
n = list(map(int, input().split()))
y = input()
m = list(map(int, input().split()))

card_dict = {a : 0 for a in m}

for i in n:
	if i in card_dict:
		card_dict[i] = 1

print(*card_dict.values())