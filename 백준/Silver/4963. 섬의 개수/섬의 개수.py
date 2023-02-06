import sys

# 인접섬을 튜플로 리턴하는 함수
def dfs(graph):
    not_repeat = []
    islands = set()
    for key in graph.keys():
        if key in not_repeat:
            continue

        else:
            
            island = [key]
            stack = [key]
            not_repeat.append(key)
            while stack:
                cur = stack.pop()

                for adj in graph[cur]:
                    if adj not in island:
                        island.append(adj)
                        stack.append(adj)
                        not_repeat.append(adj)
            
            islands.add(tuple(island))
        
    return(islands)


while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a + b == 0:break # 0, 0 입력 받으면 빠져나가기

    jido = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(b)] # 지도 생성


    points = {}
    # print(points)
    for i in range(b):
        for j in range(a):
            if jido[i][j] == 1:
                val = []
                #인접 노드들을 검색
                for k in range(-1, 2):
                    if k+i not in range(b):
                        continue
                    for l in range(-1, 2):
                        #지도의 범의를 벗어난 경우 
                        if l+j not in range(a):
                            continue
                        elif (k == 0 and l == 0):
                            continue
                        else:
                            if jido[k+i][l+j] == 1:
                                val.append(a*(k+i)+(l+j))
                points[(a*i)+j] = val
    # print(points)

    print(len(dfs(points)))