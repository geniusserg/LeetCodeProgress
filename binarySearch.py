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
        print(l, r)
    if (nums[l] == target):
        return l
    elif (nums[r] == target):
        return r
    else:
        return -1      

print(solve([-1,0,3,5,9,12], 5))
