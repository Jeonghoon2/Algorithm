# 피보나치 수
# 피보나치 수는 F(0) = 0, F(1) = 1
# 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용 되는 수
# ex ) F(2) = F(0) + F(1) = 0 + 1 = 1
# ex ) F(3) = F(1) + F(2) = 1 + 1 = 2
# ex ) F(4) = F(2) + F(3) = 1 + 2 = 3
# ex ) F(5) = F(3) + F(4) = 2 + 3 = 5

def solution(n):
    d = [0,1]
    for i in range(2, n + 1):
        d.append(d[i-1] + d[i-2])
    return d[i]%1234567

print(solution(5))