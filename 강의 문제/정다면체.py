# 정다면체
# 두 개의 정 N면체와 M면체 두 개의 주사위를 던져서 
# 나올수 있는 눈의 합 중 가장 확률이 높은 숫자는

N, M = map(int,input().split())
cnt = [0]*(N+M+1)
max = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1

for i in range(N+M+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end='')
