from data_structures.core.stack import Stack
import pytest

class TestStack:
    
    def test_init_and_empty(self):
        stack = Stack()
        assert len(stack) == 0
        assert stack.is_empty() is True

    def test_push_and_len(self):
        stack = Stack()
        stack.push('A')
        stack.push('B')
        stack.push('C')
        
        assert len(stack) == 3
        assert stack.is_empty() is False

    def test_lifo_behavior(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty() is True

    def test_peek(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)

        assert stack.peek() == 20
        assert len(stack) == 2
        
        assert stack.pop() == 20
        assert stack.peek() == 10

    def test_pop_on_empty_raises_error(self):
        stack = Stack()
        with pytest.raises(IndexError, match="Cannot pop from an empty stack."):
            stack.pop()

    def test_peek_on_empty_raises_error(self):
        stack = Stack()
        with pytest.raises(IndexError, match="Cannot peek at an empty stack."):
            stack.peek()