def max_energy_boost(energyDrinkA, energyDrinkB):
    n = len(energyDrinkA)
    
    # Base case for the first hour
    dpA = [0] * n
    dpB = [0] * n
    
    dpA[0] = energyDrinkA[0]
    dpB[0] = energyDrinkB[0]
    
    for i in range(1, n):
        if i == 1:
            dpA[i] = dpA[i-1] + energyDrinkA[i]
            dpB[i] = dpB[i-1] + energyDrinkB[i]
        else:
            dpA[i] = max(dpA[i-1] + energyDrinkA[i], dpB[i-2] + energyDrinkA[i])
            dpB[i] = max(dpB[i-1] + energyDrinkB[i], dpA[i-2] + energyDrinkB[i])
    
    return max(dpA[-1], dpB[-1])

# Example usage:
print(max_energy_boost([1, 3, 1], [3, 1, 1]))  # Output: 5
print(max_energy_boost([4, 1, 1], [1, 1, 3]))  # Output: 7


# Time complexity - O(n)
# Space Complexity - O(n)