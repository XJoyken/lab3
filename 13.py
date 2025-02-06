def has_33(nums):
    check = False
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            check = True
    print(check)

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])