# 격자판 최대합

# N*N의 N입력
N=int(input())

# 배열 저장
a = [list(map(int,input().split())) for _ in range(N)]

# 가로 세로 최댓값 구하기
for i in range(N):
    sum1=sum2=0
    max = -2147000000
    for j in range(N):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > max:
        max = sum1
    if sum2 > max:
        max = sum2
        
# 대각선 최댓값구하기
sum1=sum2=0
for i in range(N):
    sum1 += a[i][i]
    sum2 += a[i][N-i-1]
if sum1 > max:
    max = sum1
if sum2 > max:
    max = sum2

print(max)


