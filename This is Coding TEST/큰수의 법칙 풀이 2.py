# 큰수의 법칙 풀이 2
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

N1SumCount1 = ( m // ( k + 1 )) * k
N2SumCount2 = m // (k+1)

result += N1 * N1SumCount1
result += N2 * N2SumCount2

print(result)

