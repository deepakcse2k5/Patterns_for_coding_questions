nums = [4,5,9,2,6,1]

def small_count_brute_force_approach(nums):
    result = []
    # edge case
    if len(nums)==0:
        return result
    for i, num in enumerate(nums):
        count = sum(val<num for val in nums[i+1:])
        result.append(count)
    return result

# print(small_count_brute_force_approach(nums=nums))
# Time complexity - O(n**2)
# Space complexity - O(n)
import bisect

def small_count(nums):
    result = []
    seen = []
    for num in reversed(nums):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)
    return list(reversed(result))

print(small_count(nums))

# print(bisect.bisect_right([1,3,6],4))


