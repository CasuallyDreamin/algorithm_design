from .array import DynamicArray

class Stack:
    def __init__(self):
        self._list = DynamicArray() 

    def __len__(self) -> int:
        return len(self._list)

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def push(self, data):
        self._list.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._list.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self._list[len(self._list) - 1]