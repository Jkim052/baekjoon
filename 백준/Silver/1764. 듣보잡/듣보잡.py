a, b = map(int, input().split())
never_heard = set()
never_seen = set()
for i in range(a):
	never_heard.add(input())
for i in range(b):
	never_seen.add(input())

never_seen_heard = never_seen & never_heard

never_seen_heard = list(never_seen_heard)

never_seen_heard.sort()

print(len(never_seen_heard))
for i in never_seen_heard:
	print(i)