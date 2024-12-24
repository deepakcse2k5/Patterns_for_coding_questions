def circular_array_loop(nums):  

    # Replace this placeholder return statement with your code
    if len(nums)==0:
      return False
    n = len(nums)
    
    def next_index(current , direction):
      if direction * nums[current] <0:
        return -1
      next_index = (current + nums[current])% n 
      if next_index<0:
        next_index +=n 
      return next_index if next_index!=current else -1
      
    for i in range(n):
      slow, fast = i, i 
      direction = nums[i]
      while True:
        slow = next_index(slow, direction)
        fast = next_index(fast, direction)
        if fast!=-1:
          fast = next_index(fast, direction)
        if slow==-1 or fast==-1 or slow==fast:
          break
      if slow!=-1 and slow==fast:
        return True
      slow = i 
      while slow!=-1:
        next_idx = next_index(slow, nums[i])
        nums[slow]=0
        slow = next_idx
    return False

nums = [2, -1, 1, 2, 2]

print(circular_array_loop(nums))