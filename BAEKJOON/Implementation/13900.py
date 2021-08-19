n = int(input())
nums = list(map(int, input().split()))
sum_num = sum(nums)
result = 0
for i in nums:
    sum_num -= i
    result += i * sum_num
print(result)