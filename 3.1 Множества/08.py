n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

count = 0
for i in range(n - 1):
    first = str(nums[i])
    second = str(nums[i + 1])
    result = set(first) & set(second) #пересечение множеств
    if len(result) == 2:
        print(nums[i])
        count = 1
if count == 0:
    print('N')
