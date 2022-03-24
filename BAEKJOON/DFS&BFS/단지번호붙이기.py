# 단지 번호 붙이기
# dfs 로 1에서 0을 만날때까지 탐색후 탐색한곳은 

def DFS(x,y):
    #범위 벗어났을 때
    if x<0 or x>=N or y<0 or y>=N:
        return False

    # 1을 만났을 때
    if graph[x][y] ==1:
        global count
        count += 1
        graph[x][y] =0
        # dx, dy 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx,ny)
        return True
    return False

N = int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int, input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
build = []
count = 0
result = 0

for i in range(N):
    for j in range(N):
        if DFS(i,j) == True:
            # 단지내 집의 수 추가
            build.append(count)
            result += 1
            count = 0

#오름차순 정렬
build.sort()
print(result)
for i in range(len(build)):
    print(build[i])
            








