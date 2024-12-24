nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1


def remove_element(nums, val):
    if len(nums)==0:
        return None

    index = 0
    while index<len(nums):
        if nums[index]==val:
            nums.remove(nums[index])
        else:
            index+=1
    return len(nums)


print(remove_element(nums1, val1))