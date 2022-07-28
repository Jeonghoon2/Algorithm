# 오큰수
# 17298번

from inspect import stack


n = int(input())
list = list(map(int, input().split()))
stack = []
ans = [-1]*n

stack.append(0)

for i in range(n):
    # 오른쪽 수가 자신 보다 작을 때
    # 검사 순 4 -> 3 -> 2 -> 1
    while stack and list[stack[-1]] < list[i]:
        ans[stack.pop()] = list[i]
    stack.append(i)

        
print(*ans)