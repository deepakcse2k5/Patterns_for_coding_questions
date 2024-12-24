from typing import List


def removeElement( nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        count =0
        if len(nums)==0:
            return 0
        while start <=end:
            if nums[start]==val:
                if nums[end]==val:
                    nums[end]='_'
                    count+=1
                    end-=1
                nums[start],nums[end] = nums[end],nums[start]
                nums[end]='_'
                count+=1
                end-=1
            else:
                 start+=1
        for num in nums:
             if num=='_':
                  nums.remove(num)
        return nums

print(removeElement([3,2,2,3], 3))