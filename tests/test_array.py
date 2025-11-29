from data_structures.core import array as array_module
import pytest

class TestStaticArray:
    
    def test_init_and_len(self):
        arr = array_module.StaticArray(5)
        assert len(arr) == 0
        assert arr._capacity == 5

    def test_insert_and_getitem(self):
        arr = array_module.StaticArray(3)
        arr.insert('A')
        arr.insert('B')
        
        assert len(arr) == 2
        assert arr[0] == 'A'
        assert arr[1] == 'B'

    def test_full_and_overflow(self):
        arr = array_module.StaticArray(2)
        arr.insert(10)
        arr.insert(20)
        
        assert arr.is_full()
        
        with pytest.raises(OverflowError):
            arr.insert(30)

    def test_setitem(self):
        arr = array_module.StaticArray(3)
        arr.insert('X')
        arr.insert('Y')
        arr[0] = 'Z'
        
        assert arr[0] == 'Z'
        assert arr[1] == 'Y'

    def test_index_out_of_bounds(self):
        arr = array_module.StaticArray(2)
        arr.insert(1)
        
        with pytest.raises(IndexError):
            _ = arr[1]
        
        with pytest.raises(IndexError):
            arr[1] = 99


def test_dynamic_array_insert_and_getitem():
    arr = array_module.DynamicArray(capacity=4)
    arr.insert(0, 'a')
    arr.insert(1, 'b')
    arr.insert(1, 'c') 

    assert arr[0] == 'a'
    assert arr[1] == 'c'
    assert arr[2] == 'b'
    assert len(arr) == 3

def test_dynamic_array_delete_and_pop():
    arr = array_module.DynamicArray(capacity=4)
    arr.append(1)
    arr.append(2)
    arr.append(3)

    popped_value = arr.pop()
    assert popped_value == 3
    assert len(arr) == 2

    arr.delete(0)
    assert arr[0] == 2
    assert len(arr) == 1

def test_dynamic_array_resize():
    arr = array_module.DynamicArray(capacity=2) 
    arr.append(1)
    arr.append(2)
    arr.append(3) 

    assert len(arr) == 3
    assert arr._capacity == 4 

def test_dynamic_array_iteration():
    arr = array_module.DynamicArray(capacity=4)
    arr.append('x')
    arr.append('y')
    arr.append('z')

    collected = []
    for item in arr:
        collected.append(item)

    assert collected == ['x', 'y', 'z']