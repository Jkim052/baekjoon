word = input()

word = word.upper()
alpa = {}

for i in word:
    if i not in alpa:
        alpa[i] = 1
    else:
        alpa[i] += 1

big = max(alpa.values())
often = []

for key, value in alpa.items():
    if alpa[key] == big:
        often.append(key)

if len(often) == 1:
    print(*often)
else:
    print('?')