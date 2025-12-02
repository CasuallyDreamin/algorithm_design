from data_structures.core.array import DynamicArray

def find_starting_stone(stones_energy: list[int], path_cost: list[int]) -> int:
    
    N = len(stones_energy)
    if N == 0:
        return -1

    energy_array = DynamicArray()
    cost_array = DynamicArray()
    
    for i in range(N):
        energy_array.append(stones_energy[i])
        cost_array.append(path_cost[i])

    net_gain = DynamicArray()
    total_gain = 0
    
    for i in range(N):
        gain = energy_array[i] - cost_array[i]
        net_gain.append(gain)
        total_gain += gain

    if total_gain < 0:
        return -1 
    
    current_fuel = 0
    starting_index = 0
    
    for i in range(N):
        current_fuel += net_gain[i]
        
        if current_fuel < 0:
            current_fuel = 0
            starting_index = i + 1
            
    return starting_index