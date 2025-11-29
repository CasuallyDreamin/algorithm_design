from .linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self._list = DoublyLinkedList()

    def __len__(self) -> int:
        return len(self._list)

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def enqueue(self, data):
        self._list.insert_at_tail(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        
        data = self._list.head.data

        self._list.delete_node(self._list.head)
        
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")
        return self._list.head.data