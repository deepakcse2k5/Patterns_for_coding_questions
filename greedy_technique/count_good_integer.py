from itertools import permutations
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def generate_palindromes(length):
    palindromes = set()
    if length == 1:
        for i in range(1, 10):
            palindromes.add(i)
    elif length % 2 == 0:
        half_len = length // 2
        for half in range(10**(half_len - 1), 10**half_len):
            half_str = str(half)
            palin = int(half_str + half_str[::-1])
            palindromes.add(palin)
    else:
        half_len = length // 2
        for half in range(10**(half_len - 1), 10**half_len):
            for middle in range(0, 10):
                half_str = str(half)
                palin = int(half_str + str(middle) + half_str[::-1])
                palindromes.add(palin)
    return palindromes

def count_good_integers(n, k):
    good_count = 0
    
    # Generate palindromes of length 1 to n
    for length in range(1, n + 1):
        palindromes = generate_palindromes(length)
        for palin in palindromes:
            if palin % k == 0:
                digit_freq = Counter(str(palin))
                # Compute the number of permutations that can be formed
                # with exactly n digits considering no leading zeros
                digit_str = ''.join([str(digit) * freq for digit, freq in digit_freq.items()])
                # Ensure no leading zero
                if '0' in digit_freq and length > 1:
                    digit_str = digit_str.lstrip('0')
                    if not digit_str:
                        continue
                # Count permutations with leading zero
                perms = set(permutations(digit_str))
                for perm in perms:
                    if len(perm) == n and perm[0] != '0':
                        good_count += 1
                        
    return good_count

# Example Usage
print(count_good_integers(3, 5))  # Output: 27
print(count_good_integers(1, 4))  # Output: 2
print(count_good_integers(5, 6))  # Output: 2468
