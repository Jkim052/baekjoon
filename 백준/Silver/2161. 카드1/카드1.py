t = int(input())

card = list(range(1, t+1))
trash = []

while len(card) > 1:
    trash.append(card.pop(0))
    card.append(card.pop(0))

print(*trash, card[0])