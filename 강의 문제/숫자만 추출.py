# 숫자만 추출
# 문자와 숫자가 섞여 있는 문자열이 주어지면 그 중 숫자만 추출
# 그 순서대로 자연수를 만든다.
# 만들어진 자연수와 그 자연수의 약수 개수를 출력

# isdecimal 0~9 까지의 숫자를 찾아 준다.

# 입력 : g0en2Ts8eSoft

s = input()
res = 0
cnt = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

for i in range (1, res+1):
    if res%i==0:
        cnt+=1

print(res,'\n',cnt)
