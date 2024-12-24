gas = [1,2,3,4,5]
cost = [3, 4, 5,1, 2]

def gas_station_journey(gas,cost):
    if sum(gas) < sum(cost):
        return -1
    curr_gas , start_index = 0, 0

    for index in range(len(gas)):
        curr_gas += curr_gas + (gas[index] - cost[index])
        if curr_gas <0:
            curr_gas=0
            start_index+=1
    return start_index


print(gas_station_journey(gas, cost))


# Time Complexity - O(n)
# Space Complexity - O(1)