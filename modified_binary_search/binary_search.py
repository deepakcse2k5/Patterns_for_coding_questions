import math
def binary_search(nums, target):

    # Replace this placeholder return statement with your code
    if len(nums)==0:
        return -1
    l , r = 0, len(nums)-1
    
    while l<=r:
        mid = math.floor(l+r/2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid+1
        else:
            r = mid-1

print(binary_search([1,6,8,10],1))


# time complexity - O(log n)
# space complecity - O(1)