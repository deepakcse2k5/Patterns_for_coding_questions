nums = [1,2,3,4,3,5]
def find_duplicates(nums):
    # edge case
    if len(nums)==0:
        return None
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            break

    slow = nums[0]

    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast

print(find_duplicates(nums))


# Time complexity - O(n)

# Space Complexity - O(1)




