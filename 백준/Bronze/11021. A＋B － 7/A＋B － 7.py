t = int(input())  # 테스트 케이스 개수 t를 입력받음

for i in range(t):  # t 만큼 반복
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a+b}')