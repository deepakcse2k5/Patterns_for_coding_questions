s = "AAABABB"
k=1

def cha_replacement(s, k):
    count = {}
    start = 0
    max_freq = 0
    for end in range(len(s)):
        count[s[end]] = 1+ count.get(s[end], 0)

        max_freq = max(max_freq, count[s[end]])
        if (end-start+1)- max_freq>k:
            count[s[start]]-=1
            start+=1

    return end-start+1

print(cha_replacement(s,k))
