arr = [2, 1, 5, 1, 3, 2]
k = 3

def max_subarray_of_size_k(arr,k):
    max_sum, curr_sum = 0,0
    start = 0
    for end in range(len(arr)):
        curr_sum+=arr[end]
        if end>=k-1:
            max_sum = max(curr_sum, max_sum)
            curr_sum-=arr[start]
            start+=1
    return max_sum

print(max_subarray_of_size_k(arr, k))

