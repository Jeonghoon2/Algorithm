# 거스름돈
# 거스름돈 500원, 100원, 50원, 10원
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 돈전의 최소 개수를 구하여라
# 돈 N은 항상 10의 배수 

n = 1260
count = 0

#큰 단위 부터
coin_type = [500, 100, 50,10]

for coin in coin_type: 
    count += n // coin # 해당 화폐로 거슬러 줄 돈 구하기
    n %= coin

print(count)