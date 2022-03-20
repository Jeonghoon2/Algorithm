# k 번째 큰 수
# 중복을 제거하는 자료 구조 set()
# 1 <= N <= 100 N장의 카드
# 1 <= K <= 50 

N, K = map(int, input().split())
s = list(map(int, input().split()))
res = set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(s[i] + s[j] + s[m])

res =list(res)
res.sort(reverse=True)

print(res[K-1])
