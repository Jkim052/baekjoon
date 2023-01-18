word = input()
de = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
letter = str()
for i in range(len(word)):
    if word[i] in de:
        continue
    else:
        letter += word[i]

print(letter)
