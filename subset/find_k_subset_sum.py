
nums = [1,3,5,21,19,7,2]
k = 10
def find_k_subset_sum(nums, k):

    subset = []

    def back_track(start, curr_subset, curr_sum):
        if curr_sum==k:
            subset.append(list(curr_subset))
            return
        if start == len(nums) or curr_sum > k:
            return
        curr_subset.append(nums[start])
        back_track(start + 1, curr_subset, curr_sum + nums[start])
        curr_subset.pop()
        back_track(start+1,curr_subset,curr_sum)
    back_track(0,[],0)
    return subset


print(find_k_subset_sum(nums, k))



