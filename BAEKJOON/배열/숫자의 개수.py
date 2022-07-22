# 숫자의 개수
# 2577번

a = int(input())
b = int(input())
c = int(input())
div = str(a * b * c)

for i in range(10):
    print(div.count(str(i)))
