import sys

# n * n 배열
# 0은 집이 없는곳, 1은 집이 있는곳
# 연결은 위, 아래, 왼쪽, 오른쪽 가능
#
# 변수
# 집갯수 카운터, 집갯수를 다 세리고 나면 1씩 증가하는 변수

graph = []
n = int(input())
cnt = 0
answer = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    x = list(map(int,input())) #n*n
    graph.append(x) # graph에 0과 1을 넣는다.
# 예시 만약 0, 0, 0 ,0 ,1 을 입력할경우
# graph에는 [0, 0, 0, 0, 1] 이렇게 들어간다.

def dfs(x, y):
    global cnt # 전역변수 
    graph[x][y] = 0
    cnt += 1
    # 위, 아래, 왼쪽, 오른쪽 탐색
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 현재 위치의 좌표가 범위 내이면서 1 일때
        if 0 <= nx <n and 0 <= ny <n and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            answer.append(dfs(i,j))
print(len(answer))
answer.sort() # 오름차순 정렬
for i in answer:
    print(i)
   