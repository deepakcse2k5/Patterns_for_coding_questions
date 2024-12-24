gas = [5,5,2,3,4]
cost = [6,3,1,5,1]

def gas_station_journey(gas, cost):
    # edge case
    if sum(gas) < sum(cost):
        return  -1
    start_index, current_gas   = 0, 0

    for i in range(len(gas)):
        current_gas += (gas[i] - cost[i])
        if current_gas<0:
            current_gas=0
            start_index = i+1
    return start_index


print(gas_station_journey(gas, cost))


# Time Complexity - O(n)
# Space Complexity - O(1)




