import pytest
from io import StringIO
import sys
from main import Node, Queue


class TestNode:
    """Test cases for Node class."""
    
    def test_node_init(self):
        """Test node initialization."""
        node = Node(5)
        assert node.value == 5
        assert node.next is None
    
    def test_node_init_different_values(self):
        """Test node with different value types."""
        node1 = Node(10)
        assert node1.value == 10
        
        node2 = Node(-5)
        assert node2.value == -5


class TestQueueInit:
    """Test cases for Queue initialization."""
    
    def test_queue_init_single_value(self):
        """Test queue initialization with a single value."""
        queue = Queue(5)
        assert queue.first is not None
        assert queue.last is not None
        assert queue.first.value == 5
        assert queue.last.value == 5
        assert queue.first is queue.last  # Single element - same node
        assert queue.length == 1
    
    def test_queue_init_creates_node(self):
        """Test that init creates a proper node."""
        queue = Queue(42)
        assert queue.first.value == 42
        assert queue.last.value == 42
        assert queue.first.next is None
        assert queue.length == 1
    
    def test_queue_init_different_values(self):
        """Test initialization with different values."""
        for val in [0, -10, 100, 99999]:
            queue = Queue(val)
            assert queue.first.value == val
            assert queue.last.value == val
            assert queue.length == 1


class TestQueueEnqueue:
    """Test cases for enqueue method."""
    
    def test_enqueue_single_value(self):
        """Test enqueuing a single value."""
        queue = Queue(1)
        queue.enqueue(2)
        
        assert queue.length == 2
        assert queue.first.value == 1
        assert queue.last.value == 2
    
    def test_enqueue_multiple_values(self):
        """Test enqueuing multiple values."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        
        assert queue.length == 4
        assert queue.first.value == 1
        assert queue.last.value == 4
    
    def test_enqueue_maintains_fifo_order(self):
        """Test that enqueue maintains FIFO order."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue in order
        assert queue.dequeue().value == 1
        assert queue.dequeue().value == 2
        assert queue.dequeue().value == 3
    
    def test_enqueue_negative_values(self):
        """Test enqueuing negative values."""
        queue = Queue(5)
        queue.enqueue(-1)
        queue.enqueue(-100)
        
        assert queue.last.value == -100
        assert queue.length == 3
    
    def test_enqueue_zero(self):
        """Test enqueuing zero."""
        queue = Queue(5)
        queue.enqueue(0)
        assert queue.last.value == 0
    
    def test_enqueue_returns_none(self):
        """Test that enqueue doesn't return anything."""
        queue = Queue(1)
        result = queue.enqueue(2)
        assert result is None


class TestQueueDequeue:
    """Test cases for dequeue method."""
    
    def test_dequeue_single_element(self):
        """Test dequeuing the only element."""
        queue = Queue(42)
        node = queue.dequeue()
        
        assert node.value == 42
        assert queue.length == 0
        assert queue.first is None
        assert queue.last is None
    
    def test_dequeue_multiple_elements(self):
        """Test dequeuing multiple elements in order."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.dequeue().value == 1
        assert queue.dequeue().value == 2
        assert queue.dequeue().value == 3
    
    def test_dequeue_empty_returns_none(self):
        """Test dequeuing from empty queue returns None."""
        queue = Queue(1)
        queue.dequeue()
        assert queue.dequeue() is None
    
    def test_dequeue_returns_node(self):
        """Test that dequeue returns the node."""
        queue = Queue(42)
        node = queue.dequeue()
        assert isinstance(node, Node)
        assert node.value == 42
    
    def test_dequeue_decrements_length(self):
        """Test that dequeue decrements length."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.length == 3
        queue.dequeue()
        assert queue.length == 2
        queue.dequeue()
        assert queue.length == 1
    
    def test_dequeue_clears_next_pointer(self):
        """Test that dequeue clears the next pointer of returned node."""
        queue = Queue(1)
        queue.enqueue(2)
        
        node = queue.dequeue()
        # The dequeued node should have next set to None after dequeue
        assert node.next is None


class TestQueuePrintQueue:
    """Test cases for print_queue method."""
    
    def test_print_single_element(self, capsys):
        """Test printing queue with single element."""
        queue = Queue(5)
        queue.print_queue()
        captured = capsys.readouterr()
        
        assert "5" in captured.out
        assert "first" in captured.out.lower()
        assert "last" in captured.out.lower()
    
    def test_print_multiple_elements(self, capsys):
        """Test printing queue with multiple elements."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.print_queue()
        captured = capsys.readouterr()
        
        # All values should be in output
        assert "1" in captured.out
        assert "2" in captured.out
        assert "3" in captured.out
        
        # Should show 1 is first, 3 is last
        output_lines = captured.out.split('\n')
        first_line = output_lines[0]
        assert first_line.startswith("1")
    
    def test_print_empty_queue(self, capsys):
        """Test printing empty queue."""
        queue = Queue(1)
        queue.dequeue()
        queue.print_queue()
        captured = capsys.readouterr()
        
        assert "empty" in captured.out.lower()
    
    def test_print_contains_dequeue_enqueue_labels(self, capsys):
        """Test that print output contains operation labels."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.print_queue()
        captured = capsys.readouterr()
        
        # Should indicate where dequeue and enqueue happen
        assert "dequeue" in captured.out.lower() or "enqueue" in captured.out.lower()
    
    def test_print_after_dequeue(self, capsys):
        """Test printing after dequeue operation."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.print_queue()
        captured = capsys.readouterr()
        
        # 1 was dequeued, should show 2 and 3
        assert "2" in captured.out
        assert "3" in captured.out


class TestQueueIntegration:
    """Integration tests for Queue."""
    
    def test_enqueue_dequeue_cycle(self):
        """Test a complete enqueue/dequeue cycle."""
        queue = Queue(1)
        values = [2, 3, 4, 5]
        
        for v in values:
            queue.enqueue(v)
        
        for v in [1] + values:
            node = queue.dequeue()
            assert node.value == v
        
        assert queue.dequeue() is None
    
    def test_alternating_enqueue_dequeue(self):
        """Test alternating enqueue and dequeue operations."""
        queue = Queue(1)
        
        queue.enqueue(2)
        assert queue.dequeue().value == 1
        
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.dequeue().value == 2
        
        assert queue.dequeue().value == 3
        assert queue.dequeue().value == 4
    
    def test_large_queue(self):
        """Test queue with many elements."""
        queue = Queue(0)
        n = 100
        
        for i in range(1, n):
            queue.enqueue(i)
        
        assert queue.length == n
        
        for i in range(n):
            node = queue.dequeue()
            assert node.value == i
        
        assert queue.length == 0
    
    def test_fifo_order_preserved(self):
        """Test that FIFO order is always preserved."""
        queue = Queue(10)
        values = [20, 30, 40, 50, 60]
        
        for v in values:
            queue.enqueue(v)
        
        all_values = [10] + values
        for expected in all_values:
            node = queue.dequeue()
            assert node.value == expected


class TestQueueEdgeCases:
    """Test edge cases for Queue."""
    
    def test_queue_with_zero(self):
        """Test queue with zero value."""
        queue = Queue(0)
        assert queue.first.value == 0
        queue.enqueue(1)
        assert queue.dequeue().value == 0
    
    def test_queue_with_negative(self):
        """Test queue with negative values."""
        queue = Queue(-5)
        queue.enqueue(-10)
        assert queue.dequeue().value == -5
        assert queue.dequeue().value == -10
    
    def test_length_consistency(self):
        """Test that length is always consistent."""
        queue = Queue(1)
        assert queue.length == 1
        
        for i in range(2, 10):
            queue.enqueue(i)
            assert queue.length == i
        
        for i in range(9, 0, -1):
            queue.dequeue()
            assert queue.length == i - 1
    
    def test_first_last_pointers_on_single_element(self):
        """Test that first and last point to same node for single element."""
        queue = Queue(42)
        assert queue.first is queue.last
        assert queue.first.value == 42
    
    def test_queue_after_empty_and_refill(self):
        """Test queue behavior after emptying and refilling."""
        queue = Queue(1)
        queue.enqueue(2)
        
        # Empty it
        queue.dequeue()
        queue.dequeue()
        
        assert queue.length == 0
        assert queue.first is None
        assert queue.last is None
        
        # Refill on empty queue
        queue.enqueue(10)
        assert queue.length == 1
        assert queue.first.value == 10
        assert queue.last.value == 10
        assert queue.first is queue.last


class TestQueueProperties:
    """Test queue properties and invariants."""
    
    def test_length_equals_node_count(self):
        """Test that length matches actual node count."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Count nodes
        count = 0
        curr = queue.first
        while curr:
            count += 1
            curr = curr.next
        
        assert queue.length == count
    
    def test_first_node_is_oldest(self):
        """Test that first node is always the oldest."""
        queue = Queue(1)
        assert queue.first.value == 1
        
        queue.enqueue(2)
        assert queue.first.value == 1
        
        queue.enqueue(3)
        assert queue.first.value == 1
        
        queue.dequeue()
        assert queue.first.value == 2
    
    def test_last_node_is_newest(self):
        """Test that last node is always the newest."""
        queue = Queue(1)
        assert queue.last.value == 1
        
        queue.enqueue(2)
        assert queue.last.value == 2
        
        queue.enqueue(3)
        assert queue.last.value == 3
        
        queue.dequeue()
        assert queue.last.value == 3
