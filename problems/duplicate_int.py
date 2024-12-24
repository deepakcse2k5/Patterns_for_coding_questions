from typing import List


def hasDuplicate( nums: List[int]) -> bool:
        # edge case
        if len(nums)==0:
            return
        set_num = set()
        for i in range(len(nums)):
            if nums[i] in set_num:
                return False
            else:
                set_num.add(nums[i])
        return True

print(hasDuplicate(nums=[1,2,3,3]))