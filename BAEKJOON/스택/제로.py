# 제로
# 10773번

n = int(input())
a = []

for i in range(n):
    b = int(input())
    if b == 0: 
        a.pop()
    else : a.append(b)


print(sum(a))

