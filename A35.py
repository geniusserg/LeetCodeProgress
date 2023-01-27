def solve(nums, target):
    l, r = 0, len(nums)-1
    while (r-l>1):
        z = (r+l)//2
        if (nums[z] == target):
            return z
        if (nums[z] < target):
            l = z
        else:
            r = z
    if (nums[l]== target):
        return l
    if (nums[r] == target):
        return r
    if (nums[l] < target and nums[r] > target):
        return r
    if (target < nums[l]):
        return l
    if (target > nums[r]):
        return r+1

print(solve([0, 2, 4, 5], -1))
