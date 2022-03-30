# 수들의 합
# N개의 수로 된 수열 A[i],A[2],---,A[N]

a, b = map(int, input().split())
N = list(map(int, input().split()))

tot = []
tot.append(N[0])

for i in range(1,a):
    
    tot.append(N[i])


