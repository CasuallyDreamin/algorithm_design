from data_structures.core.array import DynamicArray
from data_structures.core.heap import OptimizedMaxHeap

def skyline_solver(rectangles: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    
    events = DynamicArray()

    for l, r, h in rectangles:
        
        events.append((l, h, 1))
        events.append((r, h, -1))
        
    sort_key = lambda e: (e[0], -e[2] * e[1], e[2])
    
    events.sort(key=sort_key)
    
    heap = OptimizedMaxHeap()
    heap.insert(0)
    
    skyline = DynamicArray()
    previous_max_height = 0
    
    for i in range(len(events)):
        x, h, type = events[i]
        
        if type == 1:
            heap.insert(h)
        else:
            heap.delete(h)
            
        current_max_height = heap.peek_max()

        if current_max_height != previous_max_height:
            skyline.append((x, current_max_height))
            previous_max_height = current_max_height
            
    return list(skyline._data[:len(skyline)])