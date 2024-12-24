nums = [48, 52, 57, 62, 68, 72, 5, 7, 12, 17, 21, 28, 33, 37, 41]
target = 5

def binary_search_rotated(nums,target):
    # edge case
    if len(nums)==0:
        return -1
    low , high = 0, len(nums)-1
    while low <=high:
        mid = low + (high-low)//2
        if nums[mid]==target:
            return mid
        if nums[low]<=nums[mid]:
            if nums[low]<target and target <= nums[mid]:
                high = mid-1
            else:
                low = mid + 1
        else:
            if nums[mid] < target and target<= nums[high]:
                low = mid+1
            else:
                high = mid - 1
            
    return -1 


print(binary_search_rotated(nums=nums, target=target))

# Time complexity - O(logn)
# Space complecity - O(1)