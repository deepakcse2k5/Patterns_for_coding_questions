strs = ["abc", "def", "ghi"]
def decode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#"+ s
    return res

def encode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        size = int(s[i:j])
        res.append(s[j+1:j+1+size])
        i = j+1+size
    return res

print(decode(strs))


print(encode("3#abc3#def3#ghi"))