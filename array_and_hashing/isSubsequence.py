from collections import defaultdict

s = "abc"
t = "ahbgdc"

def isSubsequence(s, t):
    string_dict = defaultdict(list(t))
    print("****",string_dict)
    for char in s:
        if char not in string_dict:
            return False
    return True

print(isSubsequence(s,t))
