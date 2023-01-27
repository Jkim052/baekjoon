import heapq

t = int(input())

words = set()
son = []

for _ in range(t):
    words.add(input())

for word in words:
    heapq.heappush(son, (len(word), word))

for _ in range(len(words)):
    print(heapq.heappop(son)[1])