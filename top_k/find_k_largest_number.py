nums = [3,1,5,2,12,11]
k=3

from heapq import *

def find_k_largest_number(number,k):
    minHeap = []
    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k,len(nums)):
        if nums[i]>minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return minHeap

print(find_k_largest_number(nums, k))


# time complexity - (O(KlogK) + (N-K)O(logK)) = NlogK
# space complexity - O(logK)