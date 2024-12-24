import math
piles = [1, 4, 2, 3]
h = 9

def minEatingSpeed(piles, h):
    l,r = 1, max(piles)

    
    res = r
    while l<=r:
        k = (l+r)//2
        total_time = 0
        for p in piles:
            total_time+= math.ceil(float(p)/k)
        if total_time<=h:
            res = k
            r = k-1
        else:
            l = k+1
    return res


print(minEatingSpeed(piles, h))

    