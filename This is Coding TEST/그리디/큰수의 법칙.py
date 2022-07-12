# 큰수의 법칙
# N 배열의 크기, M 더해지는 횟수, K 연속으로 나타낼수 있는 횟수

# 공백으 구분
n, m, k = map(int, input().split())

data = list(map(int,input().split()))

# 입력 받은 수 정렬
data.sort()

# 가장 큰수
N1 = data[n-1] 
# 두번째로 큰수
N2 = data[n-2]

result = 0

while True:
    #가장 큰수 K번 더하기
    for i in range(k):
        # m이 0이면 탈출
        if m == 0:
            break
        result += N1
        m -= 1 # m을 1씩 감소
    # m이 0이면 탈출
    if m == 0:
        break
    #두번째로 큰수 한 번 더하기
    result += N2
    m -= 1

print(result)

