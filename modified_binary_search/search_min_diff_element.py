nums = [4, 6, 10]
key = 7

def search_min_diff_element(nums, key):
    if key< nums[0]:
        return nums[0]
    n = len(nums)
    if key > nums[n-1]:
        return nums[n-1]
    start, end = 0, n-1
    while start<= end:
        mid = start + (end-start)//2
        if key < nums[mid]:
            end = mid - 1
        elif key > nums[mid]:
            start = mid+1
        else:
            return nums[mid]
    
    if (nums[start]- key) < (key-nums[end]):
        return nums[start]
    return nums[end]

print(search_min_diff_element(nums, key))

# Time Complexity - O(logn)
# Space Complexity - O(1)