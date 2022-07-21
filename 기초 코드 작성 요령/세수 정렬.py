# 세수 정렬
# 2757

N = list(map(int,input().split()))
N.sort()

for i in range(len(N)):
    print(N[i], end= " ")
