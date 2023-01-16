pop = int(input())
ans = {0 : 0, 1 : 0}
for i in range(pop):
    ans[int(input())] += 1

if ans[0] > ans[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')