from data_structures.core.heap import MaxHeap, MinHeap
import pytest

class TestMaxHeap:

    def test_init_and_empty(self):
        heap = MaxHeap()
        assert len(heap) == 0
        assert heap.is_empty() is True

    def test_insert_single_element(self):
        heap = MaxHeap()
        heap.insert(10)
        
        assert len(heap) == 1
        assert heap.peek_max() == 10

    def test_peek_on_empty_raises_error(self):
        heap = MaxHeap()
        with pytest.raises(IndexError, match="Cannot peek_max from an empty heap."):
            heap.peek_max()

    def test_extract_on_empty_raises_error(self):
        heap = MaxHeap()
        with pytest.raises(IndexError, match="Cannot extract_max from an empty heap."):
            heap.extract_max()

    def test_max_heap_property_simple(self):
        heap = MaxHeap()
        heap.insert(5)
        heap.insert(10)
        heap.insert(3)
        
        assert heap.peek_max() == 10
        
        assert heap._items[0] == 10

    def test_heapify_up_complex(self):
        heap = MaxHeap()

        heap.insert(1) 
        heap.insert(10)
        heap.insert(5) 
        heap.insert(20)
        
        assert len(heap) == 4
        assert heap.peek_max() == 20
        
        assert heap._items[1] <= 20
        assert heap._items[2] <= 20


    def test_extract_max_and_heapify_down(self):
        heap = MaxHeap()
        
        for val in [10, 5, 20, 1, 15]:
            heap.insert(val)
            
        assert heap.peek_max() == 20
        
        assert heap.extract_max() == 20
        assert len(heap) == 4
        
        assert heap.peek_max() == 15
        
        assert heap.extract_max() == 15
        assert heap.peek_max() == 10
        
        assert heap.extract_max() == 10
        assert heap.extract_max() == 5
        assert heap.extract_max() == 1
        
        assert heap.is_empty() is True

class TestMinHeap:

    def test_init_and_empty(self):
        heap = MinHeap()
        assert len(heap) == 0
        assert heap.is_empty() is True

    def test_insert_and_peek_single_element(self):
        heap = MinHeap()
        heap.insert(50)
        
        assert len(heap) == 1
        assert heap.peek_min() == 50

    def test_min_heap_property_simple(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(15)
        
        # 5 should be the root
        assert heap.peek_min() == 5
        assert heap._items[0] == 5

    def test_heapify_up_complex(self):
        heap = MinHeap()
        heap.insert(20) 
        heap.insert(5)  
        heap.insert(15) 
        heap.insert(1)
        
        assert len(heap) == 4
        assert heap.peek_min() == 1
        
        assert heap._items[1] >= 1
        assert heap._items[2] >= 1

    def test_extract_min_and_heapify_down(self):
        heap = MinHeap()
        
        for val in [20, 15, 10, 5, 1]:
            heap.insert(val)
            
        assert heap.peek_min() == 1
        
        assert heap.extract_min() == 1
        assert len(heap) == 4
        
        assert heap.peek_min() == 5
        
        assert heap.extract_min() == 5
        assert heap.peek_min() == 10
        
        assert heap.extract_min() == 10
        assert heap.extract_min() == 15
        assert heap.extract_min() == 20
        
        assert heap.is_empty() is True