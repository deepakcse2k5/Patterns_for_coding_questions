import math


def find_max_min(myList):
    if len(myList) == 0:
        return (0, 0)
    global_max, global_min = - math.inf, +math.inf
    for item in myList:
        global_max = max(global_max, item)
        global_min = min(global_min, item)

    return (global_max, global_min)


print(find_max_min([5, 3, 8, 1, 1,6, 9]))