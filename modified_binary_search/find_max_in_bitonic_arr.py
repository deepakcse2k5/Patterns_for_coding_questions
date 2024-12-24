nums = [1, 3, 8, 12, 4, 2]

def find_max_in_bitonic_arr(nums):
    start , end = 0, len(nums)-1
    while start < end:
        mid = start + (end-start)//2
        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid+1
    return start

print(find_max_in_bitonic_arr(nums))