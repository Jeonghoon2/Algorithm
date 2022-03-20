# 대표값
# N명의 학생의 수학성적이 주어진다.
# N명의 학생들의 평균을 구하고
# N명의 학생 중 평균에 가까운 학생은 몇 번 인지
# N(5<= N <= 100) 

N = int(input())
K = list(map(int,input().split()))
ave = round( sum(K) / N )
min=214700000
for idx, x in enumerate(K):
    tmp = abs(x - ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    # 만약 거리가 같은 학생을 만났을 때
    # socre 점수가 높은 학생으로 바꾼다.
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)