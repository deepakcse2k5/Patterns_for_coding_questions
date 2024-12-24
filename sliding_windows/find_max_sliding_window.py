nums = [2,-3,4,-5,7,-1,9,8]

k = 3

import math
# def find_max_sliding_window(nums, k):

#     # Replace this placeholder return statement with your code
#     if len(nums)<=0 and k<=0:
#         return []

#     result = []
#     for i in range(len(nums)-k+1):
#         max_value = - math.inf
#         for j in range(i,i+k):
#             max_value = max(max_value,nums[j])
#         result.append(max_value)

#     return result


def find_max_sliding_window(nums, k):
    if len(nums)<=0 and k<=0:
        return []
    
    result = []
    start = 0
    max_value = nums[start]
    for end in range(len(nums)):
        max_value = max(max_value, nums[end-start+1])
        if end > k:
            result.append(max_value)
            start+=1

        



print(find_max_sliding_window(nums, k))
