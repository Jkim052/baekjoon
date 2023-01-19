num = {
    '0' : 0,
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0
}

A = int(input())
B = int(input())
C = int(input())

multiple = str(A*B*C)

for i in multiple:
    num[i] += 1

for key, value in num.items():
    print(value)