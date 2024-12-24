nums = [3,2,1,0,4]

def jump_games(nums):
    # edge case
    if len(nums)==0:
        return True

    target_index = len(nums)-1
    for i in range(len(nums)-2, -1,-1):
        if target_index <= i+nums[i]:
            target_index = i
        else:
            return False
    return True

print(jump_games(nums))
