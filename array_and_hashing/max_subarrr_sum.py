arr = [8,-1,5,-1,-2,3,-3,4]

def max_subarray_sum(arr):
    curr_sum, max_sum  = 0, 0
    if len(arr)==0:
        return 0
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            curr_sum = sum(arr[i:j+1])
            max_sum = max(curr_sum, max_sum)

    return max_sum

print(max_subarray_sum(arr=arr))


# kadane's algorithm

def max_sum_arr(arr):
    # edge case
    if len(arr)==0:
        return 0
    max_end_here , max_end_so_far = 0, 0
    for num in arr:
        max_end_here = max(num, max_end_here+num)
        max_end_so_far = max(max_end_so_far, max_end_here)
    return max_end_so_far

print(max_sum_arr(arr=arr))

def min_sub_arr(arr):
    min_end_here , min_end_so_far = 0, 0
    for num in arr:
        min_end_here = min(num, min_end_here+num)
        min_end_so_far = min(min_end_here, min_end_so_far)
    return min_end_so_far

def max_sum_subarr_wrapup(arr):
    max_end_so_far_wrapup = sum(arr) - min_sub_arr(arr)
    max_end_so_far_wrapup = max(max_end_so_far_wrapup, max_sum_arr(arr))
    return max_end_so_far_wrapup


print(max_sum_subarr_wrapup(arr))

