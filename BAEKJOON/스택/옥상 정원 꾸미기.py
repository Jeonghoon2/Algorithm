# 옥상 정원 꾸미기
# 시간 초과 ㅠㅠ

n = int(input())
building = []
answer = [0 for i in range(n)]
for i in range(n): building.append(int(input()))

for i in range(n):
    
    for j in range(i,n):
        if building[i] < building[j]:
            break
        elif building[i] == building[j]:
            continue
        else:
            answer[i] = answer[i] + 1

print(sum(answer))
