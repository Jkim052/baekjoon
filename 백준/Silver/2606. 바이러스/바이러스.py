n = int(input())
t = int(input())

# 리스트 생성
computers = [[] for _ in range(n)]

for i in range(t):
    a, b = map(int, input().split())
    computers[a-1].append(b-1)
    computers[b-1].append(a-1)

visited = [False]* n
visited[0] = True
stack = [0]

while stack:
    for i in computers[stack.pop()]:
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            
print(sum(visited)-1)