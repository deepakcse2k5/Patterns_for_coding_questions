from typing import List
import math


def maxSlidingWindow( nums: List[int], k: int) -> List[int]:
        # edge case
        if len(nums)==0 or k==0:
            return []
        if len(nums)<k:
            return nums

        result = []
        start = 0
        new_list =[]

        for end in range(len(nums)):
            
            new_list.append(nums[end])
            if (end-start+1)>k-1:
                max_val =  max(new_list)
                result.append(max_val)
                new_list.remove(nums[start])
                start+=1
            
        return result

print(maxSlidingWindow([1,2,1,0,4,2,6], k=3))