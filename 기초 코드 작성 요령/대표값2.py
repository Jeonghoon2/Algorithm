list = []
avg = 0
for i in range(5):
    A = int(input())
    list.append(A)

list.sort()
avg = sum(list)//5
print(avg)
print(list[2])