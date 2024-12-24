import math
nums = [3,4,5,6,1,2]

def find_min(nums):
    # edge case
    if len(nums)==0:
        return 0
    start , end = 0, len(nums) - 1
    curr_min = + math.inf

    while start < end:
        mid = start + (end-start)//2
        curr_min = min(curr_min, nums[mid])

        if nums[mid] > nums[end]:
            start = mid+1
        else:
            end = mid-1
    return min(curr_min, nums[start])


print(find_min(nums))
