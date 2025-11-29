from data_structures.core import linked_list as ll_module
import pytest

class TestSinglyLinkedList:
    
    def test_init_and_len(self):
        sll = ll_module.SinglyLinkedList()
        assert len(sll) == 0
        assert sll.head is None

    def test_insert_at_head(self):
        sll = ll_module.SinglyLinkedList()
        sll.insert_at_head(10)
        sll.insert_at_head(20)

        assert len(sll) == 2
        assert sll.head.data == 20
        assert sll.head.next_node.data == 10

    def test_insert_at_tail(self):
        sll = ll_module.SinglyLinkedList()
        sll.insert_at_head(10)
        sll.insert_at_tail(30)
        
        current = sll.head
        while current.next_node:
            current = current.next_node

        assert len(sll) == 2
        assert sll.head.data == 10
        assert current.data == 30

    def test_delete_by_value(self):
        sll = ll_module.SinglyLinkedList()
        sll.insert_at_head(1)
        sll.insert_at_head(2)
        sll.insert_at_head(3)
        
        # Delete middle element
        assert sll.delete_by_value(2) is True
        assert len(sll) == 2
        assert sll.head.data == 3
        assert sll.head.next_node.data == 1

        assert sll.delete_by_value(3) is True
        assert len(sll) == 1
        assert sll.head.data == 1

        assert sll.delete_by_value(1) is True
        assert len(sll) == 0
        assert sll.head is None

        assert sll.delete_by_value(99) is False

    def test_iteration(self):
        sll = ll_module.SinglyLinkedList()
        sll.insert_at_tail('a')
        sll.insert_at_tail('b')
        sll.insert_at_tail('c')
        
        collected = [item for item in sll]
        assert collected == ['a', 'b', 'c']

class TestDoublyLinkedList:

    def test_init_and_pointers(self):
        dll = ll_module.DoublyLinkedList()
        dll.insert_at_head(5)
        
        assert dll.head.data == 5
        assert dll.tail.data == 5
        assert dll.head.prev_node is None
        assert dll.tail.next_node is None

    def test_insert_at_head_and_tail(self):
        dll = ll_module.DoublyLinkedList()
        dll.insert_at_head(1)
        dll.insert_at_tail(3)
        dll.insert_at_head(0)

        assert len(dll) == 3
        assert dll.head.data == 0
        assert dll.tail.data == 3
        
        assert dll.tail.prev_node.data == 1
        assert dll.head.next_node.data == 1
        
    def test_delete_node(self):
        dll = ll_module.DoublyLinkedList()
        dll.insert_at_tail(10)
        dll.insert_at_tail(20)
        dll.insert_at_tail(30)
        
        node_to_delete = dll.head.next_node
        
        # Delete middle node
        assert dll.delete_node(node_to_delete) is True
        assert len(dll) == 2
        assert dll.head.next_node.data == 30
        assert dll.tail.prev_node.data == 10

        # Delete head
        assert dll.delete_node(dll.head) is True
        assert dll.head.data == 30
        assert dll.head.prev_node is None
        assert dll.tail.data == 30

        # Delete last node (tail)
        assert dll.delete_node(dll.head) is True
        assert len(dll) == 0
        assert dll.head is None
        assert dll.tail is None

    def test_reverse_traversal(self):
        dll = ll_module.DoublyLinkedList()
        dll.insert_at_tail(1)
        dll.insert_at_tail(2)
        dll.insert_at_tail(3)
        
        collected = []
        current = dll.tail
        while current:
            collected.append(current.data)
            current = current.prev_node
            
        assert collected == [3, 2, 1]

class TestCircularLinkedList:
    
    def test_init(self):
        cll = ll_module.CircularLinkedList()
        assert len(cll) == 0
        assert cll.tail is None

    def test_insert_single_node(self):
        cll = ll_module.CircularLinkedList()
        cll.insert_at_head(10)
        
        assert len(cll) == 1
        assert cll.tail.data == 10
        assert cll.tail.next_node.data == 10

    def test_insert_at_head_and_tail(self):
        cll = ll_module.CircularLinkedList()
        cll.insert_at_head(1)
        cll.insert_at_tail(3)
        cll.insert_at_head(0)
        
        assert len(cll) == 3
        
        assert cll.tail.next_node.data == 0
        assert cll.tail.data == 3
        assert cll.tail.next_node.next_node.next_node.next_node.data == 0

    def test_full_circle_iteration(self):
        cll = ll_module.CircularLinkedList()
        cll.insert_at_tail('a')
        cll.insert_at_tail('b')
        cll.insert_at_tail('c')
        
        collected = [item for item in cll]
        assert collected == ['a', 'b', 'c']

        assert cll.tail.next_node.data == 'a'