import sys
sys.setrecursionlimit(10000)

### split ###
#  split은 문자열을 나눌 때 사용한다.
#  괄호 안에 아무것도 넣지 않으면 공백(띄어쓰기, 탭등)을 기준으로 문자열을 나눈다.
#  나누어진 값은 리스트의 요소로 저장되는데, 
#  분활된 무자의 개수만큼 각각을 변수로 지정하는 것도 가능하다.


def init_graph(graph, k):
    m, n = map(int,input().split())
    graph[n][m] = 1

    return graph

# 탐색할때 x나 y가 0 이하가 되거나 x와 y가 N값 보다 크거나 같을때
# 탐색을 멈춘다.
 
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    
    if graph[x][y] == 1: # 배추가 심어져 있을 경우
        graph[x][y] = 0 # 배추가 안심어져 있을 경우
        dfs(x-1,y)#상
        dfs(x+1,y)#하
        dfs(x,y-1)#좌
        dfs(x,y+1)#우
        return True
    return False

#반복 횟수
T = int(input())

for _ in range(T):
    #가로, 세로, 배추의 수
    M,N,K = map(int,input().split())
    cnt = 0
    #배추밭 초기화
    graph = [[0]*M for _ in range(N)]
    graph = init_graph(graph, K)
    
    for i in range(N):
        for j in range(M):
            dfs(i,j)
    print(ans)



