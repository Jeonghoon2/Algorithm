p, q = map(int,input().split())
a = []
for x in range(1,p+1):
    if p%x==0:
        a.append(x)
    if len(a)==q:
        print(x)
        break
else:
    print(0)