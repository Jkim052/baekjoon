from pprint import pprint
# 변수 입력 받기
king, stone, n = map(str, input().split())
moves = [input() for _ in range(int(n))]

alpa = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}

chess = range(8)
# 움직임
move = {
'R' : (1, 0),
'L' : (-1, 0),
'B' : (0, -1),
'T' : (0, 1),
'RT' : (1, 1),
'LT' : (-1, 1),
'RB' : (1, -1),
'LB' : (-1, -1)
}
#킹이랑 돌 체스판 위에 위치하기
king = (alpa[king[0]], int(king[1])-1)
stone = (alpa[stone[0]], int(stone[1])-1)

for i in moves:
    a = king[0] + move[i][0]
    b = king[1] + move[i][1]
    if (a in chess) and (b in chess):# 킹을 움직였는데 범위 안에 있다면
        if stone == (a, b): # 킹의 위치랑 돌의 위치가 같다면
            c = stone[0] + move[i][0] 
            d = stone[1] + move[i][1]
            if (c in chess) and (d in chess): #돌을 움직인였는데 범위 안에 있다면
                king = (a, b) 
                stone = (c, d) #킹과 돌을 움직인다
        else: # 킹을 움직였는데 돌을 건드리지 않았다면
            king = (a, b)
beta = {v:k for k,v in alpa.items()}

king = beta[king[0]]+str(king[1]+1)
stone = beta[stone[0]]+str(stone[1]+1)

print(king, stone)
