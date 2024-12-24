from heapq import *
start_fuel = 10
target = 120
stations = [[10, 60], [20, 25], [30, 30],[60,40]]

def min_refuel_stops(target, start_fuel, stations):
    maxHeap = []
    if start_fuel>= target:
        return 0
    
    i , n = 0, len(stations)
    stops = 0
    max_distance = start_fuel
    while max_distance < target:
        if i < n and stations[i][0] <= max_distance:
            heappush(maxHeap, -stations[i][1])
            i+=1
        elif not maxHeap:
            return -1
        else:
            max_distance += -heappop(maxHeap)
            stops+=1
    return stops

print(min_refuel_stops(target, start_fuel, stations))


# Time Complexity - O(nlogn)
# Space Compexity - O(n)





