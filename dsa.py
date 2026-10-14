nums = [8, 2, 3, 4]
target = 7
sorted_num = sorted(nums)
length = len(nums)
left = 0
right = length - 1
while left < right:
    sums = sorted_num[left] + sorted_num[right]
    if target == sums:
        print([nums.index(sorted_num[left]), nums.index(sorted_num[right])])
    elif sums < target:
        left += 1
    else:
        right -= 1



