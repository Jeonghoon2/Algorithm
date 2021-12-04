# 1이 될 때 까지2
# 두가지의 방법으로 N을 1로 만들기 위한 최소한의 횟수를 구하여야 하는 문제
# 첫번째 방법 : N에서 1을 뺀다.
# 두번째 방법 : N을 K로 나눈다.

N, K = map(int, input().split())

result = 0

while True:

    if N == 1:
        break

    if (N // K) != 0:
        N-=1
        result+=1
        

    if (N // K) > 0:
        N //= K
        result += 1
        

print(result)