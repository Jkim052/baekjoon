a = input()

if a == a[-1 : -(len(a)+1) : -1]:
    print(1)
else:
    print(0)