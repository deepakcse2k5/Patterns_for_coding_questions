def max_additional_diners(N, K, M, S):
    # Step 1: Create a list to mark unavailable seats
    unavailable = [False] * (N + 1)  # Using N + 1 to handle 1-based indexing
    
    # Step 2: Mark seats around each existing diner
    for seat in S:
        start = max(1, seat - K)
        end = min(N, seat + K)
        for i in range(start, end + 1):
            unavailable[i] = True
    
    # Step 3: Count the number of available segmentss
            
    count = 0
    i = 1
    while i <= N:
        if not unavailable[i]:
            # Start of a new free segment
            start = i
            while i <= N and not unavailable[i]:
                i += 1
            end = i - 1
            # Calculate the number of diners that can fit in this segment
            length = end - start + 1
            if length > 0:
                count += (length + 1) // (K + 1)
        else:
            i += 1
    
    return count

# Example usage
N = 10
K = 1
M = 2
S = [2, 6]
print(max_additional_diners(N, K, M, S))  # Output: 3

N = 15
K = 2
M = 3
S = [11, 6, 14]
print(max_additional_diners(N, K, M, S))  # Output: 1
