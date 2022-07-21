# 방 배정
# 13300

import math


n, c = map(int, input().split())
st = [[0]*6 for _ in range(2)]

for _ in range(n):
    s, a = map(int, input().split())
    st[s][a-1] += 1

room = 0
for i in st:
    for j in i:
        room += math.ceil(j/c)
        
print(room)