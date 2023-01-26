t = int(input())

num_list = []

for i in range(t):
    num = int(input())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()

print(sum(num_list))