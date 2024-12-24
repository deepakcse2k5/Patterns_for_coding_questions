import math
def smallest_subarray_sum(s, arr):
  # TODO: Write your code here
  if len(arr)==0:
    return -1

  curr_sum,start = 0, 0
  min_length = + math.inf

  for end in range(len(arr)):
    curr_sum += arr[end]
    while curr_sum>=s :
      min_length = min(min_length, end-start+1)
      curr_sum-=arr[start]
      start+=1
    
  return min_length


s = 7
arr = [2,1,5,2,3,2]

print(smallest_subarray_sum(s, arr)) #2