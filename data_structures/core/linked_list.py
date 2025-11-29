class SinglyNode:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.prev_node = None
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def insert_at_head(self, data):
        new_node = SinglyNode(data)
        new_node.next_node = self.head
        self.head = new_node
        self._size += 1

    def insert_at_tail(self, data):
        new_node = SinglyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self._size += 1

    def delete_by_value(self, target_data):
        current = self.head
        prev = None
        
        while current and current.data != target_data:
            prev = current
            current = current.next_node
        
        if not current:
            return False

        if not prev:
            self.head = current.next_node
        else:
            prev.next_node = current.next_node
        
        self._size -= 1
        return True
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def insert_at_head(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        self._size += 1

    def insert_at_tail(self, data):
        new_node = DoublyNode(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        self._size += 1

    def delete_node(self, node):
        if not node:
            return False

        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node
            
        self._size -= 1
        return True

class CircularLinkedList:
    def __init__(self):
        self.tail = None 
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        if not self.tail:
            return
        
        current = self.tail.next_node
        head = current
        
        while True:
            yield current.data
            current = current.next_node
            if current == head:
                break

    def insert_at_head(self, data):
        new_node = SinglyNode(data)
        if not self.tail:
            self.tail = new_node
            new_node.next_node = new_node
        else:
            new_node.next_node = self.tail.next_node
            self.tail.next_node = new_node
        self._size += 1

    def insert_at_tail(self, data):
        if not self.tail:
            self.insert_at_head(data)
        else:
            self.insert_at_head(data)
            self.tail = self.tail.next_node