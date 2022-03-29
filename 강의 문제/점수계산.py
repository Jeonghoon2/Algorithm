# 점수 계산
# 10
# 1 0 1 1 1 0 0 1 1 0 

N = int(input())
sol = map(int, input().split())
total = 0
pre = 0
for i in sol:
    if i == 1:
        pre += 1
        total += pre
    if i == 0:
        pre = 0

print(total)
