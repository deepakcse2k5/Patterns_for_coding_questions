from typing import List
nums = [1,2,1]

def getConcatenation(nums: List[int]) -> List[int]:
        ans = 2*[0]*len(nums)
        n = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans

print(getConcatenation(nums))