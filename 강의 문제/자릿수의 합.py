# 자릿수의 합

N = int(input())
a = list(map(int, input().split()))
max = 0

def digit_sum(x):
    sum =0
    while x > 0:
        sum += x%10
        x = x//10
    return sum

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max =tot
        res = x
print(res)
        
# 다른 풀이

N = int(input())
a = list(map(int, input().split()))
max = 0

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum =+ int(i)
    return sum

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max =tot
        res = x
print(res)

        