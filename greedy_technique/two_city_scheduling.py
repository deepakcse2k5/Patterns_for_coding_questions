costs = [[10, 20], [30, 200], [400, 50], [30, 20]]


def two_city_scheduling(costs):
    total_cost = 0
    costs.sort(key=lambda x:abs(x[0]-x[1]))
    cost_length = len(costs)

    for index in range(cost_length//2):
        total_cost = total_cost+ costs[index][0] + costs[cost_length-index-1][1]

    return total_cost


print(two_city_scheduling(costs))


# Time Complexity - O(nlogn)
# Space complexity - O(n)