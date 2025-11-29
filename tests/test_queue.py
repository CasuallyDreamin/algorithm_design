from data_structures.core.queue import Queue
import pytest

class TestQueue:
    
    def test_init_and_empty(self):
        queue = Queue()
        assert len(queue) == 0
        assert queue.is_empty() is True

    def test_enqueue_and_len(self):
        queue = Queue()
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        
        assert len(queue) == 3
        assert queue.is_empty() is False

    def test_fifo_behavior(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty() is True

    def test_peek(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)

        assert queue.peek() == 10
        assert len(queue) == 2
        
        assert queue.dequeue() == 10
        assert queue.peek() == 20

    def test_dequeue_on_empty_raises_error(self):
        queue = Queue()
        with pytest.raises(IndexError, match="Cannot dequeue from an empty queue."):
            queue.dequeue()

    def test_peek_on_empty_raises_error(self):
        queue = Queue()
        with pytest.raises(IndexError, match="Cannot peek at an empty queue."):
            queue.peek()