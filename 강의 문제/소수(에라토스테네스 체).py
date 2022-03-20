# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1 부터 N까지의 소수

N = int(input())
count =0
def solve(x):
    if (x<2):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

for i in range(N+1):
    if(solve(i)):
        count += 1
print(count)
