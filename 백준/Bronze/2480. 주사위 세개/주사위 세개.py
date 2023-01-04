a, b, c = map(int, input().split())
if a!=b and b!=c and a!=c:
    print(max(a,b,c)*100)
elif a==b and b==c and a==c:
    print(a*1000+10000)
else:
    if a==b:
        print(a*100+1000)
    elif a==c:
        print(a*100+1000)
    else:
        print(b*100+1000)