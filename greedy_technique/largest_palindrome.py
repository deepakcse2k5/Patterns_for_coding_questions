from collections import Counter
nums = "454352882"

def largest_palindrome(nums):
    num_freq = Counter(nums)

    first_half = []
    middle = ""
    for digit in range(9,1,-1):
        digit_char = str(digit)

        if digit_char in num_freq:
            digit_count = num_freq[digit_char]

            num_pairs = digit_count//2
            if num_pairs:
                if not first_half and not digit:
                    num_freq["0"]=1
                else:
                    first_half.append(digit_char * num_pairs)
            if digit_count%2 and not middle:
                middle = digit_char

    if not middle and not first_half:
        return "0"
    return "".join(first_half + [middle] + first_half[::-1])

print(largest_palindrome(nums))

# Time Complexity - O(n)
# Space Complexity - O(n)


