

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]

k =5

def avg_arr_brute_force(arr,k):
    # get average value of array
    result = []
    for i in range(len(arr)-k+1):
        _sum =0.0
        for j in range(i,i+k):
            _sum+=arr[j]
        result.append(_sum/k)
    return result

def find_avg_of_subarray(arr,k):
    # edge case
    if len(arr)==0:
        return []
    result = []
    sum, start = 0.0, 0
    for end in range(len(arr)):
        sum+=arr[end]
        if end>= k-1:
            result.append(sum/k)
            sum-= arr[start]
            start+=1
    return result

def main():
    result = find_avg_of_subarray(arr, k)
    print(f"Average of subarray of sizek:{result}")

main()





