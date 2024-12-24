def isAnagram(s: str, t: str) -> bool:
        # edge case
        if len(s)==0 and len(t)==0:
            return True
        freq_map = {}
        for char in s:
            if char in freq_map:
                freq_map[char]+=1
            else:
                freq_map[char]=1
        for char in t:
            if char in freq_map:
                freq_map[char]-=1
        if sum(list(freq_map.values()))==0:
            return True
        return False
s="bbcc"
t="ccbc"
print(isAnagram(s, t))