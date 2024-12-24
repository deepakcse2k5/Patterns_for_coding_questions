nums = [2,3,1,1,4]

def jump_games(nums):
    # edge case
    target_index = len(nums)-1
    for index in range(len(nums)-2, -1, -1):
        if target_index <= index +nums[index]:
            target_index = index
    if target_index==0:
        return True
    return False


print(jump_games(nums))

# Time complexity - O(n)
# Space Complexity - O(1)
        


    
