from typing import List


def rob(nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])

        def rob_linear(house):
            prev1, prev2 = 0, 0
            for num in nums:
                temp = max( prev1, prev2+num)
                prev2 = prev1
                prev1 = temp
            return prev1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

print(rob([3,4,3]))