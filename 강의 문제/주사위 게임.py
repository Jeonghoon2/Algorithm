# 주사위 게임

# 1에서 6까지의 눈을 가진 3개의 주사위를 던진다.
# 1. 같은 눈이 3개가 나오면 10,000 + ( 같은눈 )*1,000원의 상금을 받게 된다.
# 2. 같은 눈이 2개가 나오면 1,000 + (같은 눈)*100원의 상금을 받게 된다.
# 3. 모두 다른 눈이 나오는 경우에는 ( 그 중 가장 큰 눈)*100원의 상금을 받게 된다.
# 첫째 줄에는 참여하는 사람 수 N(2 <= N <= 1,0000)이 주어진다.

import random

N = int(input())

res=0

for j in range(N):
    # dice1 = random.randrange(1,7)
    # dice2 = random.randrange(1,7)
    # dice3 = random.randrange(1,7)
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int,tmp)
    if a==b and b==c:
        money = 10000+ (a*1000)
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money= c * 100

    if money>res:
        res = money

print(res)