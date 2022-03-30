# 카드 역배치
# 1 부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 오름차순으로 한 줄로 놓여 있다.

import sys
sys.stdin = open("/Users/jeonghun/Desktop/IT/Algorithms/강의 문제/input.txt", 'rt')

a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i],a[e-i] = a[e-i],a[s+i]
print(a)

