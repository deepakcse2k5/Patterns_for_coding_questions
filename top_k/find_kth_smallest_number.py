nums = [1,5,12,2,11,3]
k = 3
from heapq import *
def find_kth_smallest_number(nums, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, -nums[i])
    
    for i in range(k, len(nums)):
        if -nums[i]> maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])
    return -maxHeap[0]

print(find_kth_smallest_number(nums, k))

# Time complexity - O(klogk) + (N-k)* logk = O(Nlogk)
# Space complexity - O(k)
