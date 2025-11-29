from .array import DynamicArray

class MaxHeap:
    def __init__(self):
        self._items = DynamicArray() 

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def _get_parent_index(self, index: int) -> int:
        if index == 0:
            return -1
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def _get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def _swap(self, i: int, j: int):
        temp = self._items[i]
        self._items[i] = self._items[j]
        self._items[j] = temp

    def _heapify_up(self, index: int):
        parent_index = self._get_parent_index(index)
        
        while index > 0 and self._items[index] > self._items[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._get_parent_index(index)

    def _heapify_down(self, index: int):
        last_index = len(self._items) - 1
        
        while True:
            left_index = self._get_left_child_index(index)
            right_index = self._get_right_child_index(index)
            largest = index

            if left_index <= last_index and self._items[left_index] > self._items[largest]:
                largest = left_index

            if right_index <= last_index and self._items[right_index] > self._items[largest]:
                largest = right_index

            if largest == index:
                break
            
            self._swap(index, largest)
            index = largest

    def insert(self, data):
        self._items.append(data)
        self._heapify_up(len(self._items) - 1)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Cannot extract_max from an empty heap.")
        
        max_val = self._items[0]
        last_index = len(self._items) - 1
        
        self._items[0] = self._items[last_index]
        
        self._items.pop() 
        
        if not self.is_empty():
            self._heapify_down(0)
            
        return max_val

    def peek_max(self):
        if self.is_empty():
            raise IndexError("Cannot peek_max from an empty heap.")
        return self._items[0]
    
class MinHeap:
    def __init__(self):
        self._items = DynamicArray() 

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def _get_parent_index(self, index: int) -> int:
        if index == 0:
            return -1
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def _get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def _swap(self, i: int, j: int):
        temp = self._items[i]
        self._items[i] = self._items[j]
        self._items[j] = temp

    def _heapify_up(self, index: int):
        parent_index = self._get_parent_index(index)
        
        # Current node is not root AND is smaller than its parent
        while index > 0 and self._items[index] < self._items[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._get_parent_index(index)

    def _heapify_down(self, index: int):
        last_index = len(self._items) - 1
        
        while True:
            left_index = self._get_left_child_index(index)
            right_index = self._get_right_child_index(index)
            smallest = index

            # Check if left child exists and is smaller
            if left_index <= last_index and self._items[left_index] < self._items[smallest]:
                smallest = left_index

            # Check if right child exists and is smaller than the current smallest
            if right_index <= last_index and self._items[right_index] < self._items[smallest]:
                smallest = right_index

            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest

    def insert(self, data):
        self._items.append(data)
        self._heapify_up(len(self._items) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Cannot extract_min from an empty heap.")
        
        min_val = self._items[0]
        last_index = len(self._items) - 1
        
        self._items[0] = self._items[last_index]
        self._items.pop() 
        
        if not self.is_empty():
            self._heapify_down(0)
            
        return min_val

    def peek_min(self):
        if self.is_empty():
            raise IndexError("Cannot peek_min from an empty heap.")
        return self._items[0]