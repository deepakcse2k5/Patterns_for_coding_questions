word = "abbababa"

def is_palindrome(word, left, right):
    while left < right:
        if word[left]!= word[right]:
            return False
        else:
            left+=1
            right-=1
    return True

def validate_palindrome(word):
    left , right = 0, len(word)-1
    while left< right:
        if word[left]!= word[right]:
            return is_palindrome(word, left+1, right) or is_palindrome(word, left, right-1)
        else:
            left+=1
            right-=1
    return True
        
        

print(validate_palindrome(word))
