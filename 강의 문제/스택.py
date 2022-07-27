# 스택
# 10828번

N = int(input())

for i in N:
    li = []
    co = list(input().split)
    if co[0] == 'push':
        li.append(co[1])
    elif co[0] == 'pop':
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop())
    elif co[0] == 'size':
        print(len(li))
    elif co[0] == 'empty':
        if len(li)==0:
            print(1)
        else:
            print(0)
    elif co[0] == 'top':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])