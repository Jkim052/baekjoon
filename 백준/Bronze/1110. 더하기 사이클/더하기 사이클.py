a = input()

if int(a) < 10:
    a = a+'0'
d = a
c=0
while True:
    if int(a[0])+int(a[-1]) >= 10:
        b = str(int(a[0])+int(a[-1])-10)
        a = a[-1]+b
    else:
        b = str(int(a[0])+int(a[-1]))
        a = a[-1]+b
    c+=1
    if d == a:break     
print(c)