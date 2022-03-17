n = int(input())
nums = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_value = -100000000
min_value = 100000000

def cal(i, list):
    global add, sub, mul, div, max_value, min_value

    if i == n:
        max_value = max(max_value, list)
        min_value = min(min_value, list)
    else:
        if add > 0:
            add -= 1
            cal(i+1, list + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            cal(i+1, list - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            cal(i+1, list * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            cal(i+1, int(list/nums[i]))
            div += 1
cal(1, nums[0])

print(max_value)
print(min_value)