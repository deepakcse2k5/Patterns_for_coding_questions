import math
str1 = "abbcb"
str2 = "ac"

def find_min_window(str1, str2):
    # edge case
    if len(str1)==0 or len(str2)==0:
        return ''
    len1 = len(str1)
    len2 = len(str2)
    min_sub_length = +math.inf
    min_subsequence = ""
    index_s1 , index_s2 = 0, 0
    while index_s1< len1:
        if str1[index_s1] == str2[index_s2]:
            index_s2+=1
        


def main():
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["bde", "kzed", "css", "la", "ab"]

    # let's uncomment the following test case and verify the result
    # str1.append("abcdedeaqdweq")
    # str2.append("aqeq")

    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", find_min_window(str1[i], str2[i]))
        print("-"*100)

main()

# Time complexity - O(n), where n is the length of string1
# space complexity - O(1)

