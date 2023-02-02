word = input()

words = []
a = len(word)
word = word[::-1]

for i in range(1, a-1):
    for j in range(i+1, a):
        b = word[j:a] + word[i:j] + word[0:i]
        words.append(b)

words.sort()

print(words[0])