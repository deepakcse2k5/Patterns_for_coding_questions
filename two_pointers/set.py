def count_substrings_with_k_constraint(s, k):
    n = len(s)
    count_0 = 0
    count_1 = 0
    start = 0
    result = 0
    
    for end in range(n):
        if s[end] == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        # If the window doesn't satisfy the k-constraint, shrink the window from the left
        while count_0 > k and count_1 > k:
            if s[start] == '0':
                count_0 -= 1
            else:
                count_1 -= 1
            start += 1
        
        # Number of valid substrings ending at `end`
        result += (end - start + 1)
    
    return result

# Example usage:
print(count_substrings_with_k_constraint("10101", 1))  # Output: 12
print(count_substrings_with_k_constraint("1010101", 2))  # Output: 25
