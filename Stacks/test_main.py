import pytest
from io import StringIO
import sys
from main import Node, Stack, sort_stack


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


class TestStackInit:
    """Test cases for Stack initialization."""
    
    def test_stack_init_single_value(self):
        """Test stack initialization with a single value."""
        stack = Stack(5)
        assert stack.top is not None
        assert stack.top.value == 5
        assert stack.height == 1
    
    def test_stack_init_creates_node(self):
        """Test that init creates a proper node."""
        stack = Stack(42)
        assert stack.top.value == 42
        assert stack.top.next is None
        assert stack.height == 1
    
    def test_stack_init_different_values(self):
        """Test initialization with different values."""
        for val in [0, -10, 100, 99999]:
            stack = Stack(val)
            assert stack.top.value == val
            assert stack.height == 1


class TestStackIsEmpty:
    """Test cases for is_empty method."""
    
    def test_is_empty_non_empty_stack(self):
        """Test is_empty on non-empty stack."""
        stack = Stack(1)
        assert stack.is_empty() is False
    
    def test_is_empty_after_push(self):
        """Test is_empty after pushing."""
        stack = Stack(1)
        stack.push(2)
        assert stack.is_empty() is False
    
    def test_is_empty_after_pop_all(self):
        """Test is_empty after popping all items."""
        stack = Stack(1)
        stack.pop()
        assert stack.is_empty() is True


class TestStackPush:
    """Test cases for push method."""
    
    def test_push_single_value(self):
        """Test pushing a single value onto the stack."""
        stack = Stack(1)
        result = stack.push(2)
        assert result is True
        assert stack.top.value == 2
        assert stack.height == 2
    
    def test_push_multiple_values(self):
        """Test pushing multiple values."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        
        assert stack.height == 4
        assert stack.top.value == 4
    
    def test_push_maintains_lifo_order(self):
        """Test that push maintains LIFO order."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        
        # Pop in reverse order
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_push_negative_values(self):
        """Test pushing negative values."""
        stack = Stack(5)
        stack.push(-1)
        stack.push(-100)
        
        assert stack.top.value == -100
        assert stack.height == 3
    
    def test_push_zero(self):
        """Test pushing zero."""
        stack = Stack(5)
        stack.push(0)
        assert stack.top.value == 0


class TestStackPop:
    """Test cases for pop method."""
    
    def test_pop_single_element(self):
        """Test popping the only element."""
        stack = Stack(42)
        val = stack.pop()
        assert val == 42
        assert stack.height == 0
        assert stack.is_empty() is True
    
    def test_pop_multiple_elements(self):
        """Test popping multiple elements in order."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_pop_empty_returns_none(self):
        """Test popping from empty stack returns None."""
        stack = Stack(1)
        stack.pop()
        assert stack.pop() is None
    
    def test_pop_returns_value_not_node(self):
        """Test that pop returns the value, not the node."""
        stack = Stack(42)
        val = stack.pop()
        assert val == 42
        assert not isinstance(val, Node)
    
    def test_pop_decrements_height(self):
        """Test that pop decrements height."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.height == 3
        stack.pop()
        assert stack.height == 2
        stack.pop()
        assert stack.height == 1


class TestStackPeek:
    """Test cases for peek method."""
    
    def test_peek_single_element(self):
        """Test peek on stack with one element."""
        stack = Stack(42)
        val = stack.peek()
        assert val == 42
    
    def test_peek_does_not_remove(self):
        """Test that peek doesn't remove the element."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        
        val1 = stack.peek()
        val2 = stack.peek()
        assert val1 == val2 == 3
        assert stack.height == 3
    
    def test_peek_after_push(self):
        """Test peek after pushing a new value."""
        stack = Stack(1)
        stack.push(100)
        assert stack.peek() == 100
    
    def test_peek_empty_returns_none(self):
        """Test peeking empty stack returns None."""
        stack = Stack(1)
        stack.pop()
        assert stack.peek() is None
    
    def test_peek_after_multiple_operations(self):
        """Test peek after multiple push/pop operations."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        
        assert stack.peek() == 2


class TestStackPrintHorizontal:
    """Test cases for print_horizontal method."""
    
    def test_print_single_element(self, capsys):
        """Test printing stack with single element."""
        stack = Stack(5)
        stack.print_horizontal()
        captured = capsys.readouterr()
        
        assert "5" in captured.out
        assert "<-" in captured.out or "top" in captured.out.lower()
    
    def test_print_multiple_elements(self, capsys):
        """Test printing stack with multiple elements."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        stack.print_horizontal()
        captured = capsys.readouterr()
        
        # All values should be in output
        assert "3" in captured.out
        assert "2" in captured.out
        assert "1" in captured.out
        
        # Should show 3 is at top (first in output)
        output_lines = captured.out.split('\n')
        first_line = output_lines[0]
        assert first_line.startswith("3")
    
    def test_print_empty_stack(self, capsys):
        """Test printing empty stack."""
        stack = Stack(1)
        stack.pop()
        stack.print_horizontal()
        captured = capsys.readouterr()
        
        assert "empty" in captured.out.lower()
    
    def test_print_contains_top_indicator(self, capsys):
        """Test that print output contains top indicator."""
        stack = Stack(42)
        stack.push(99)
        stack.print_horizontal()
        captured = capsys.readouterr()
        
        assert "top" in captured.out.lower()


class TestStackIntegration:
    """Integration tests for Stack."""
    
    def test_push_pop_cycle(self):
        """Test a complete push/pop cycle."""
        stack = Stack(1)
        values = [2, 3, 4, 5]
        
        for v in values:
            stack.push(v)
        
        for v in reversed(values):
            assert stack.pop() == v
        
        assert stack.pop() == 1
        assert stack.pop() is None
    
    def test_alternating_push_pop(self):
        """Test alternating push and pop operations."""
        stack = Stack(1)
        
        stack.push(2)
        assert stack.pop() == 2
        
        stack.push(3)
        stack.push(4)
        assert stack.pop() == 4
        
        assert stack.peek() == 3
        assert stack.pop() == 3
        assert stack.pop() == 1
    
    def test_large_stack(self):
        """Test stack with many elements."""
        stack = Stack(0)
        n = 100
        
        for i in range(1, n):
            stack.push(i)
        
        assert stack.height == n
        
        for i in range(n - 1, -1, -1):
            assert stack.pop() == i


class TestSortStack:
    """Test cases for sort_stack function."""
    
    def test_sort_stack_empty(self):
        """Test sort_stack on empty stack."""
        stack = Stack(1)
        stack.pop()
        result = sort_stack(stack)
        # sort_stack returns None, just verify it doesn't crash
        assert stack.height == 0
    
    def test_sort_stack_single_element(self):
        """Test sort_stack with single element."""
        stack = Stack(42)
        sort_stack(stack)
        # Single element should remain unchanged
        assert stack.peek() == 42
    
    def test_sort_stack_two_elements(self):
        """Test sort_stack with two elements."""
        stack = Stack(2)
        stack.push(1)
        sort_stack(stack)
        
        # Should be sorted in ascending order from bottom to top
        assert stack.pop() == 1
        assert stack.pop() == 2
    
    def test_sort_stack_three_elements(self):
        """Test sort_stack with three elements."""
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        sort_stack(stack)
        
        # After sorting, should pop in order 1, 2, 3
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
    
    def test_sort_stack_example_from_main(self):
        """Test sort_stack with the example from main."""
        stack = Stack(2)
        stack.push(4)
        stack.push(3)
        stack.push(1)
        sort_stack(stack)
        
        # Expected order from bottom to top: 1, 2, 3, 4
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
        assert stack.pop() == 4
    
    def test_sort_stack_already_sorted(self):
        """Test sort_stack on already sorted stack."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        sort_stack(stack)
        
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
        assert stack.pop() == 4
    
    def test_sort_stack_reverse_sorted(self):
        """Test sort_stack on reverse sorted stack."""
        stack = Stack(4)
        stack.push(3)
        stack.push(2)
        stack.push(1)
        sort_stack(stack)
        
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
        assert stack.pop() == 4
    
    def test_sort_stack_with_duplicates(self):
        """Test sort_stack with duplicate values."""
        stack = Stack(3)
        stack.push(1)
        stack.push(3)
        stack.push(1)
        sort_stack(stack)
        
        assert stack.pop() == 1
        assert stack.pop() == 1
        assert stack.pop() == 3
    
    def test_sort_stack_with_negative_numbers(self):
        """Test sort_stack with negative numbers."""
        stack = Stack(5)
        stack.push(-3)
        stack.push(2)
        stack.push(-1)
        sort_stack(stack)
        
        assert stack.pop() == -3
        assert stack.pop() == -1
        assert stack.pop() == 2
        assert stack.pop() == 5
    
    def test_sort_stack_large_values(self):
        """Test sort_stack with larger values."""
        stack = Stack(1000)
        stack.push(100)
        stack.push(10000)
        stack.push(1)
        sort_stack(stack)
        
        assert stack.pop() == 1
        assert stack.pop() == 100
        assert stack.pop() == 1000
        assert stack.pop() == 10000


class TestStackEdgeCases:
    """Test edge cases for Stack."""
    
    def test_stack_with_zero(self):
        """Test stack with zero value."""
        stack = Stack(0)
        assert stack.peek() == 0
        stack.push(0)
        assert stack.pop() == 0
    
    def test_stack_with_negative(self):
        """Test stack with negative values."""
        stack = Stack(-5)
        stack.push(-10)
        assert stack.pop() == -10
        assert stack.peek() == -5
    
    def test_height_consistency(self):
        """Test that height is always consistent."""
        stack = Stack(1)
        assert stack.height == 1
        
        for i in range(2, 10):
            stack.push(i)
            assert stack.height == i
        
        for i in range(9, 0, -1):
            stack.pop()
            assert stack.height == i - 1
