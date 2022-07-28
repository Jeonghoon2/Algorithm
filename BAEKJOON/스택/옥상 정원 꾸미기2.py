# 옥상 정원 꾸미기
# 시간 초과 ㅠㅠ

n = int(input())
building = []
pointbuilding = 0
count =0

for i in range(n): building.append(int(input()))

for i in range(n):
    pointbuilding = building[i]
    j = 0
    j = j + i
    while i <= n-1:
        if j == 6:
            break
        elif pointbuilding < building[j]:
            j+=1
            break
        elif pointbuilding == building[j]:
            j+=1
            continue
        else:
            count += 1
            j+=1

print(count)
