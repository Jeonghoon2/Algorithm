# N과 M (2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

n,m = list(map(int,input().split())) # N과 M 입력을 받는다.
s = [] # m개의 수열을 저장하기 위한 리스트

def dfs(start):
    if len(s)==m: # s의 수열이 m개 되면 들어있는 모든 수열을 출력하기 위해
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s: # s안에 i가 있는지 없는지 확인
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)