class StaticArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity = capacity
        self._data = [None] * capacity 
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int):
        if not (0 <= index < self._capacity):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def __setitem__(self, index: int, value):
        if not (0 <= index < self._capacity):
            raise IndexError("Index out of bounds")
        if self._data[index] is None:
            self._size += 1
        self._data[index] = value

    def insert(self, value):
        if self._size >= self._capacity:
            raise OverflowError("Array is full, cannot insert.")
        self._data[self._size] = value
        self._size += 1

    def is_full(self) -> bool:
        return self._size == self._capacity

class ArrayIterator:
    def __init__(self, array_instance):
        self._array = array_instance
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._array):
            item = self._array[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

class DynamicArray:
    def __init__(self, capacity: int = 1):
        self._capacity = capacity
        self._data = self._make_array(self._capacity)
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def __setitem__(self, index: int, value):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def __iter__(self):
        return ArrayIterator(self)

    def _make_array(self, capacity: int):
        return [None] * capacity

    def _resize(self, new_capacity: int):
        new_data = self._make_array(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        self._data[self._size] = value
        self._size += 1

    def insert(self, index: int, value):
        if not (0 <= index <= self._size):
            raise IndexError("Index out of bounds")

        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
        
        self._data[index] = value
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Cannot pop from empty array.")
        
        self._size -= 1
        return self._data[self._size]

    def delete(self, index: int):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i+1]
        
        self._size -= 1
        self._data[self._size] = None

    def remove_value(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                self.delete(i)
                return
        raise ValueError("Value not found in array.")

    def sort(self, key=None):
        if self._size <= 1:
            return
        self._merge_sort_recursive(0, self._size - 1, key)

    def _merge_sort_recursive(self, start: int, end: int, key=None):
        if start >= end:
            return
        
        mid = (start + end) // 2
        
        self._merge_sort_recursive(start, mid, key)
        self._merge_sort_recursive(mid + 1, end, key)
        
        self._merge_subarrays(start, mid, end, key)

    def _merge_subarrays(self, start: int, mid: int, end: int, key=None):
    
        size = end - start + 1
        aux_data = self._make_array(size) 

        for i in range(size):
            aux_data[i] = self._data[start + i]

        i = 0
        j = mid - start + 1
        k = start


        len_l = mid - start + 1

        while i < len_l and j < size:
            item_l = aux_data[i]
            item_r = aux_data[j]
            

            key_l = key(item_l) if key else item_l
            key_r = key(item_r) if key else item_r

            if key_l <= key_r:
                self._data[k] = item_l
                i += 1
            else:
                self._data[k] = item_r
                j += 1
            k += 1


        while i < len_l:
            self._data[k] = aux_data[i]
            i += 1
            k += 1

        while j < size:
            self._data[k] = aux_data[j]
            j += 1
            k += 1