nums = [2, 5, 7]

def get_bit(num, bit):
    temp = (1<<bit)
    temp = temp & num
    if temp==0:
        return 0
    else:
        return 1
def find_all_subsets(nums):
    subsets = []
    if not nums:
        return [[]]
    else:
        subset_count = 2**(len(nums))
        for i in range(subset_count):
            subset = set()
            for j in range(len(nums)):
                if get_bit(i,j)==1 and nums[j] not in subset:
                    subset.add(nums[j])
            if i==0:
                subsets.append([])
            else:
                subsets.append(list(subset))
    return subsets

print(find_all_subsets(nums))

# Time complexity - O(n2**n)
# Space complexity - O(n)

