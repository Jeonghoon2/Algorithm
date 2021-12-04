# 숫자 카드 게임
# min(), max() 함수를 이용 
N, M = map(int, input().split())

result = 0
# 한줄씩 입력 받아 확인
for i in range(N):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수를 min_value에 저장
    min_value = min(data)
    # result와 min_value중 에서 가장 큰 수를 result에 저장
    result = max(result, min_value)
print(result)
