# 키로거
# 5397
# -- 아직 풀지 못한 문제 --


from turtle import left, right


n = int(input())

def encode(x):
    left =[]
    right = []
    for i in x:
        if i == '<':
            if left:
                right.append(left.pop)
        elif i == '>':
            if right:
                left.append(right.pop)
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))

for _ in range(n):  
    a = input()
    print(encode(a))




