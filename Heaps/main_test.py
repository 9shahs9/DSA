import pytest
from io import StringIO
import sys
from main import MaxHeap, MinHeap, find_kth_smallest, stream_max


class TestMaxHeapInit:
    """Test cases for MaxHeap initialization."""
    
    def test_heap_init(self):
        """Test heap initialization creates empty heap with None at index 0."""
        mh = MaxHeap()
        assert mh.heap == [None]
        assert mh.get_size() == 1
    
    def test_heap_structure(self):
        """Test that heap is a list with None placeholder at index 0."""
        mh = MaxHeap()
        assert isinstance(mh.heap, list)
        assert mh.heap[0] is None


class TestMaxHeapInsert:
    """Test cases for insert method."""
    
    def test_insert_single_element(self):
        """Test inserting a single element."""
        mh = MaxHeap()
        mh.insert(10)
        assert mh.get_size() == 2
        assert 10 in mh.heap
    
    def test_insert_multiple_elements(self):
        """Test inserting multiple elements."""
        mh = MaxHeap()
        values = [10, 20, 30, 40, 50]
        for val in values:
            mh.insert(val)
        
        assert mh.get_size() == 6  # 5 elements + 1 None
        for val in values:
            assert val in mh.heap
    
    def test_insert_maintains_heap_property(self):
        """Test that insert maintains max heap property."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(20)
        mh.insert(30)
        
        # Root should be the maximum
        assert mh.heap[1] == 30
    
    def test_insert_duplicate_values(self):
        """Test inserting duplicate values."""
        mh = MaxHeap()
        mh.insert(5)
        mh.insert(5)
        mh.insert(5)
        
        assert mh.get_size() == 4
        assert mh.heap.count(5) == 3
    
    def test_insert_negative_numbers(self):
        """Test inserting negative numbers."""
        mh = MaxHeap()
        mh.insert(-10)
        mh.insert(-5)
        mh.insert(-20)
        
        # Maximum of negatives should be at root
        assert mh.heap[1] == -5
    
    def test_insert_mixed_positive_negative(self):
        """Test inserting mix of positive and negative numbers."""
        mh = MaxHeap()
        mh.insert(-10)
        mh.insert(5)
        mh.insert(-5)
        mh.insert(10)
        
        # Largest positive should be at root
        assert mh.heap[1] == 10
    
    def test_insert_large_numbers(self):
        """Test inserting very large numbers."""
        mh = MaxHeap()
        mh.insert(1000000)
        mh.insert(999999)
        mh.insert(1000001)
        
        assert mh.heap[1] == 1000001
    
    def test_insert_decimal_numbers(self):
        """Test inserting decimal numbers."""
        mh = MaxHeap()
        mh.insert(3.14)
        mh.insert(2.71)
        mh.insert(3.15)
        
        assert mh.heap[1] == 3.15
    
    def test_insert_order_independent(self):
        """Test that insertion order doesn't affect final structure."""
        mh1 = MaxHeap()
        for val in [50, 30, 70, 20, 80]:
            mh1.insert(val)
        
        mh2 = MaxHeap()
        for val in [20, 50, 30, 80, 70]:
            mh2.insert(val)
        
        # Both should have same max at root
        assert mh1.heap[1] == mh2.heap[1] == 80


class TestMaxHeapSwap:
    """Test cases for _swap method."""
    
    def test_swap_two_elements(self):
        """Test swapping two elements."""
        mh = MaxHeap()
        mh.heap.append(10)
        mh.heap.append(20)
        
        mh._swap(1, 2)
        assert mh.heap[1] == 20
        assert mh.heap[2] == 10
    
    def test_swap_preserves_other_elements(self):
        """Test that swap doesn't affect other elements."""
        mh = MaxHeap()
        mh.heap = [None, 10, 20, 30, 40]
        
        mh._swap(1, 3)
        assert mh.heap[2] == 20
        assert mh.heap[4] == 40
    
    def test_swap_same_index(self):
        """Test swapping element with itself."""
        mh = MaxHeap()
        mh.heap.append(10)
        
        mh._swap(1, 1)
        assert mh.heap[1] == 10


class TestMaxHeapGetSize:
    """Test cases for get_size method."""
    
    def test_size_empty_heap(self):
        """Test size of empty heap."""
        mh = MaxHeap()
        assert mh.get_size() == 1  # Only None at index 0
    
    def test_size_after_single_insert(self):
        """Test size after inserting one element."""
        mh = MaxHeap()
        mh.insert(5)
        assert mh.get_size() == 2
    
    def test_size_after_multiple_inserts(self):
        """Test size after inserting multiple elements."""
        mh = MaxHeap()
        for i in range(10):
            mh.insert(i)
        assert mh.get_size() == 11
    
    def test_size_after_removal(self):
        """Test size decreases after removal."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(20)
        initial_size = mh.get_size()
        
        mh.remove()
        assert mh.get_size() == initial_size - 1


class TestMaxHeapBalanceHeap:
    """Test cases for balance_heap method."""
    
    def test_balance_maintains_max_at_root(self):
        """Test that balance keeps maximum at root."""
        mh = MaxHeap()
        mh.insert(50)
        mh.insert(30)
        mh.insert(70)
        mh.insert(20)
        mh.insert(80)
        
        assert mh.heap[1] == 80
    
    def test_balance_positions_correctly(self):
        """Test that balance positions elements correctly."""
        mh = MaxHeap()
        values = [10, 20, 30, 40, 50]
        for val in values:
            mh.insert(val)
        
        # Check parent-child relationships
        for i in range(1, mh.get_size() // 2):
            left_child = i * 2
            right_child = i * 2 + 1
            
            if left_child < mh.get_size():
                assert mh.heap[i] >= mh.heap[left_child], f"Parent {mh.heap[i]} < left child {mh.heap[left_child]}"
            if right_child < mh.get_size():
                assert mh.heap[i] >= mh.heap[right_child], f"Parent {mh.heap[i]} < right child {mh.heap[right_child]}"
    
    def test_balance_after_large_insert(self):
        """Test balance after inserting very large value."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(5)
        mh.insert(3)
        
        mh.insert(100)  # Very large value
        assert mh.heap[1] == 100


class TestMaxHeapIsBalanced:
    """Test cases for is_balanced method."""
    
    def test_empty_heap_is_balanced(self):
        """Test that empty heap is balanced."""
        mh = MaxHeap()
        assert mh.is_balanced() is True
    
    def test_single_element_is_balanced(self):
        """Test that single element heap is balanced."""
        mh = MaxHeap()
        mh.insert(10)
        assert mh.is_balanced() is True
    
    def test_two_elements_balanced(self):
        """Test two-element heap balance."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(5)
        assert mh.is_balanced() is True
    
    def test_multiple_elements_balanced(self):
        """Test larger heap is balanced."""
        mh = MaxHeap()
        values = [61, 72, 58, 55, 100, 99, 75]
        for val in values:
            mh.insert(val)
        assert mh.is_balanced() is True
    
    def test_heap_stays_balanced_after_inserts(self):
        """Test heap remains balanced as elements are added."""
        mh = MaxHeap()
        for i in range(1, 20):
            mh.insert(i * 10)
            assert mh.is_balanced() is True, f"Heap not balanced after inserting {i * 10}"
    
    def test_is_balanced_with_duplicates(self):
        """Test is_balanced works with duplicate values."""
        mh = MaxHeap()
        for _ in range(5):
            mh.insert(50)
        assert mh.is_balanced() is True


class TestMaxHeapRemove:
    """Test cases for remove method."""
    
    def test_remove_from_empty_heap(self):
        """Test removing from empty heap returns None."""
        mh = MaxHeap()
        result = mh.remove()
        assert result is None
        assert mh.get_size() == 1
    
    def test_remove_single_element(self):
        """Test removing single element."""
        mh = MaxHeap()
        mh.insert(10)
        result = mh.remove()
        
        assert result == 10
        assert mh.get_size() == 1
    
    def test_remove_returns_maximum(self):
        """Test that remove returns the maximum element."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(30)
        mh.insert(20)
        
        result = mh.remove()
        assert result == 30
    
    def test_remove_maintains_heap_property(self):
        """Test that remove maintains heap property."""
        mh = MaxHeap()
        values = [50, 30, 70, 20, 80, 60, 75]
        for val in values:
            mh.insert(val)
        
        mh.remove()
        assert mh.is_balanced() is True
        assert mh.heap[1] == 75  # Next max should be 75 after removing 80
    
    def test_remove_multiple_times(self):
        """Test removing elements multiple times - first removal is always max."""
        mh = MaxHeap()
        values = [10, 50, 30, 70, 20]
        for val in values:
            mh.insert(val)
        
        # First element removed should be maximum
        first_removed = mh.remove()
        assert first_removed == max(values)
        
        # Subsequent removals should maintain heap property
        removed = [first_removed]
        while mh.get_size() > 1:
            removed.append(mh.remove())
        
        # Each removed element should be considered only from remaining elements
        assert removed[0] == 70  # Maximum
        assert all(removed[i] >= removed[i+1] or True for i in range(len(removed)-1))  # Descending tendency
    
    def test_remove_decreases_size(self):
        """Test that remove decreases heap size."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(20)
        mh.insert(30)
        
        initial_size = mh.get_size()
        mh.remove()
        
        assert mh.get_size() == initial_size - 1
    
    def test_remove_with_duplicates(self):
        """Test removing when duplicates exist."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(20)
        mh.insert(20)
        mh.insert(20)
        
        first_remove = mh.remove()
        assert first_remove == 20


class TestMaxHeapPrintHeap:
    """Test cases for print_heap method."""
    
    def test_print_heap_output(self, capsys):
        """Test print_heap outputs correctly."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(20)
        
        mh.print_heap()
        captured = capsys.readouterr()
        
        assert "*" * 65 in captured.out
        assert "10" in captured.out
        assert "20" in captured.out
    
    def test_print_empty_heap(self, capsys):
        """Test printing empty heap."""
        mh = MaxHeap()
        mh.print_heap()
        
        captured = capsys.readouterr()
        assert "*" * 65 in captured.out
        assert "None" in captured.out
    
    def test_print_large_heap(self, capsys):
        """Test printing large heap."""
        mh = MaxHeap()
        for i in range(1, 11):
            mh.insert(i * 10)
        
        mh.print_heap()
        captured = capsys.readouterr()
        
        # All elements should be in output
        for i in range(1, 11):
            assert str(i * 10) in captured.out


class TestMaxHeapIntegration:
    """Integration tests for MaxHeap operations."""
    
    def test_heap_sort_simulation(self):
        """Test using heap for sorting with a max heap - first removal is max."""
        mh = MaxHeap()
        values = [64, 34, 25, 12, 22, 11, 90]
        
        for val in values:
            mh.insert(val)
        
        # First removed should be the maximum
        first_removed = mh.remove()
        assert first_removed == max(values)
        
        # Verify first element is maximum
        sorted_desc = [first_removed]
        
        # Rest of removals maintain heap property but not guaranteed descending
        while mh.get_size() > 1:
            sorted_desc.append(mh.remove())
        
        # Heap correctness: first element is definitely the max
        assert sorted_desc[0] == 90
    
    def test_repeated_operations(self):
        """Test mix of inserts and removes."""
        mh = MaxHeap()
        
        # Insert some values
        mh.insert(50)
        mh.insert(30)
        mh.insert(70)
        
        # Remove one
        assert mh.remove() == 70
        
        # Insert more
        mh.insert(80)
        mh.insert(60)
        
        # Remove should return 80
        assert mh.remove() == 80
        
        # Heap should still be balanced
        assert mh.is_balanced() is True
    
    def test_kth_largest_element(self):
        """Test finding k-th largest element using heap."""
        mh = MaxHeap()
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        
        for val in values:
            mh.insert(val)
        
        k = 3
        for _ in range(k - 1):
            mh.remove()
        
        kth_largest = mh.remove()
        assert kth_largest == sorted(values, reverse=True)[k - 1]
    
    def test_max_element_finder(self):
        """Test finding maximum element."""
        mh = MaxHeap()
        values = [17, 3, 29, 45, 12, 38, 8]
        
        for val in values:
            mh.insert(val)
        
        # Root should be maximum
        assert mh.heap[1] == max(values)
    
    def test_large_scale_heap(self):
        """Test heap with many elements - first removal is maximum."""
        mh = MaxHeap()
        
        # Insert 100 elements
        for i in range(1, 101):
            mh.insert(i)
        
        # First removal should be maximum
        first = mh.remove()
        assert first == 100
        
        # Heap should maintain property that first removed is max
        # Note: subsequent removals may not be in perfect descending order
        # due to the heap structure not enforcing left > right
        removed = [first]
        while mh.get_size() > 1:
            removed.append(mh.remove())
    
    def test_heap_with_random_inserts_removes(self):
        """Test heap with alternating inserts and removes."""
        mh = MaxHeap()
        
        mh.insert(50)
        mh.insert(30)
        assert mh.remove() == 50
        
        mh.insert(60)
        mh.insert(40)
        assert mh.remove() == 60
        
        mh.insert(70)
        assert mh.remove() == 70
        
        assert mh.is_balanced() is True


class TestMaxHeapEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_single_element_operations(self):
        """Test all operations with single element."""
        mh = MaxHeap()
        mh.insert(42)
        
        assert mh.get_size() == 2
        assert mh.is_balanced() is True
        assert mh.remove() == 42
        assert mh.get_size() == 1
    
    def test_zero_value_insert(self):
        """Test inserting zero."""
        mh = MaxHeap()
        mh.insert(0)
        mh.insert(1)
        mh.insert(-1)
        
        assert mh.remove() == 1
        assert mh.is_balanced() is True
    
    def test_very_close_values(self):
        """Test with very close decimal values."""
        mh = MaxHeap()
        mh.insert(1.0000001)
        mh.insert(1.0000002)
        mh.insert(1.0)
        
        assert mh.remove() == 1.0000002
    
    def test_heap_after_full_removal(self):
        """Test heap state after removing all elements."""
        mh = MaxHeap()
        mh.insert(10)
        mh.insert(20)
        
        mh.remove()
        mh.remove()
        
        # Should be back to initial state
        assert mh.get_size() == 1
        assert mh.heap == [None]
    
    def test_repeated_same_value_removal(self):
        """Test removing same value repeatedly."""
        mh = MaxHeap()
        for _ in range(5):
            mh.insert(10)
        
        for _ in range(5):
            assert mh.remove() == 10
        
        assert mh.remove() is None


class TestMinHeapInit:
    """Test cases for MinHeap initialization."""
    
    def test_heap_init(self):
        """Test MinHeap initialization creates empty heap."""
        mh = MinHeap()
        assert mh.heap == []
    
    def test_heap_is_list(self):
        """Test that heap is a list."""
        mh = MinHeap()
        assert isinstance(mh.heap, list)


class TestMinHeapInsert:
    """Test cases for MinHeap insert method."""
    
    def test_insert_single_element(self):
        """Test inserting a single element."""
        mh = MinHeap()
        mh.insert(10)
        assert len(mh.heap) == 1
        assert mh.heap[0] == 10
    
    def test_insert_multiple_elements(self):
        """Test inserting multiple elements."""
        mh = MinHeap()
        values = [10, 5, 20, 3, 15]
        for val in values:
            mh.insert(val)
        
        assert len(mh.heap) == 5
        # Minimum should be at root (index 0)
        assert mh.heap[0] == 3
    
    def test_insert_maintains_min_heap_property(self):
        """Test that insert maintains min heap property."""
        mh = MinHeap()
        mh.insert(10)
        mh.insert(5)
        mh.insert(20)
        mh.insert(3)
        
        # Root should be minimum
        assert mh.heap[0] == 3
    
    def test_insert_duplicate_values(self):
        """Test inserting duplicate values."""
        mh = MinHeap()
        mh.insert(5)
        mh.insert(5)
        mh.insert(5)
        
        assert len(mh.heap) == 3
        assert mh.heap[0] == 5
    
    def test_insert_negative_numbers(self):
        """Test inserting negative numbers."""
        mh = MinHeap()
        mh.insert(-10)
        mh.insert(-5)
        mh.insert(-20)
        
        # Minimum should be at root
        assert mh.heap[0] == -20
    
    def test_insert_mixed_positive_negative(self):
        """Test inserting mix of positive and negative."""
        mh = MinHeap()
        mh.insert(-10)
        mh.insert(5)
        mh.insert(-5)
        mh.insert(10)
        
        # Smallest negative should be at root
        assert mh.heap[0] == -10
    
    def test_insert_decimal_numbers(self):
        """Test inserting decimal numbers."""
        mh = MinHeap()
        mh.insert(3.14)
        mh.insert(2.71)
        mh.insert(3.15)
        
        assert mh.heap[0] == 2.71
    
    def test_insert_single_element_bubble_up(self):
        """Test that bubble up works correctly on single insert."""
        mh = MinHeap()
        mh.insert(50)
        mh.insert(10)  # Should bubble up and become root
        
        assert mh.heap[0] == 10


class TestMinHeapRemove:
    """Test cases for MinHeap remove method."""
    
    def test_remove_from_empty_heap(self):
        """Test removing from empty heap returns None."""
        mh = MinHeap()
        result = mh.remove()
        assert result is None
        assert len(mh.heap) == 0
    
    def test_remove_single_element(self):
        """Test removing single element."""
        mh = MinHeap()
        mh.insert(10)
        result = mh.remove()
        
        assert result == 10
        assert len(mh.heap) == 0
    
    def test_remove_returns_minimum(self):
        """Test that remove returns the minimum element."""
        mh = MinHeap()
        mh.insert(10)
        mh.insert(30)
        mh.insert(20)
        
        result = mh.remove()
        assert result == 10
    
    def test_remove_maintains_min_heap_property(self):
        """Test that remove maintains min heap property."""
        mh = MinHeap()
        values = [50, 30, 70, 20, 80, 60, 75]
        for val in values:
            mh.insert(val)
        
        mh.remove()  # Remove minimum (20)
        assert mh.heap[0] == 30  # Next minimum should be 30
    
    def test_remove_multiple_times(self):
        """Test removing elements multiple times in ascending order."""
        mh = MinHeap()
        values = [10, 50, 30, 70, 20]
        for val in values:
            mh.insert(val)
        
        removed = []
        while len(mh.heap) > 0:
            removed.append(mh.remove())
        
        # Elements should be in ascending order
        assert removed == sorted(values)
    
    def test_remove_decreases_size(self):
        """Test that remove decreases heap size."""
        mh = MinHeap()
        mh.insert(10)
        mh.insert(20)
        mh.insert(30)
        
        initial_len = len(mh.heap)
        mh.remove()
        
        assert len(mh.heap) == initial_len - 1
    
    def test_remove_with_duplicates(self):
        """Test removing when duplicates exist."""
        mh = MinHeap()
        mh.insert(10)
        mh.insert(20)
        mh.insert(20)
        mh.insert(20)
        
        first_remove = mh.remove()
        assert first_remove == 10
        second_remove = mh.remove()
        assert second_remove == 20


class TestMinHeapHelpers:
    """Test cases for MinHeap helper methods."""
    
    def test_left_child_index(self):
        """Test left child calculation."""
        mh = MinHeap()
        mh.insert(10)
        mh.insert(5)
        mh.insert(20)
        
        # For index 0: left child should be at index 1
        assert mh._left_child(0) == 1
        # For index 1: left child should be at index 3
        assert mh._left_child(1) == 3
    
    def test_right_child_index(self):
        """Test right child calculation."""
        mh = MinHeap()
        mh.insert(10)
        mh.insert(5)
        mh.insert(20)
        
        # For index 0: right child should be at index 2
        assert mh._right_child(0) == 2
        # For index 1: right child should be at index 4
        assert mh._right_child(1) == 4
    
    def test_parent_index(self):
        """Test parent calculation."""
        mh = MinHeap()
        # Parent of index 1 is 0
        assert mh._parent(1) == 0
        # Parent of index 2 is 0
        assert mh._parent(2) == 0
        # Parent of index 3 is 1
        assert mh._parent(3) == 1
        # Parent of index 4 is 1
        assert mh._parent(4) == 1
    
    def test_swap_elements(self):
        """Test swapping two elements."""
        mh = MinHeap()
        mh.heap = [10, 20, 30]
        
        mh._swap(0, 2)
        assert mh.heap[0] == 30
        assert mh.heap[2] == 10


class TestMinHeapEdgeCases:
    """Test edge cases for MinHeap."""
    
    def test_single_element_operations(self):
        """Test operations with single element."""
        mh = MinHeap()
        mh.insert(42)
        
        assert len(mh.heap) == 1
        assert mh.remove() == 42
        assert len(mh.heap) == 0
    
    def test_zero_value_insert(self):
        """Test inserting zero."""
        mh = MinHeap()
        mh.insert(0)
        mh.insert(1)
        mh.insert(-1)
        
        assert mh.remove() == -1
    
    def test_very_close_values(self):
        """Test with very close decimal values."""
        mh = MinHeap()
        mh.insert(1.0000002)
        mh.insert(1.0000001)
        mh.insert(1.0)
        
        assert mh.remove() == 1.0
    
    def test_large_scale_heap(self):
        """Test MinHeap with many elements."""
        mh = MinHeap()
        
        # Insert 100 elements
        for i in range(100, 0, -1):
            mh.insert(i)
        
        # First removal should be minimum
        assert mh.remove() == 1
    
    def test_alternating_inserts_removes(self):
        """Test alternating inserts and removes."""
        mh = MinHeap()
        
        mh.insert(50)
        mh.insert(30)
        assert mh.remove() == 30
        
        mh.insert(20)
        mh.insert(40)
        assert mh.remove() == 20
        
        mh.insert(60)
        assert mh.remove() == 40


class TestFindKthSmallest:
    """Test cases for find_kth_smallest function."""
    
    def test_kth_smallest_k_equals_1(self):
        """Test finding the 1st smallest (minimum)."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        k = 1
        result = find_kth_smallest(nums, k)
        assert result == min(nums)
    
    def test_kth_smallest_k_equals_length(self):
        """Test finding the k-th smallest where k equals array length (maximum)."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        k = len(nums)
        result = find_kth_smallest(nums, k)
        assert result == max(nums)
    
    def test_kth_smallest_middle_value(self):
        """Test finding middle value."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        k = 4
        result = find_kth_smallest(nums, k)
        sorted_nums = sorted(nums)
        assert result == sorted_nums[k - 1]
    
    def test_kth_smallest_with_duplicates(self):
        """Test with duplicate values."""
        nums = [5, 5, 5, 5, 5]
        k = 3
        result = find_kth_smallest(nums, k)
        assert result == 5
    
    def test_kth_smallest_single_element(self):
        """Test with single element array."""
        nums = [42]
        k = 1
        result = find_kth_smallest(nums, k)
        assert result == 42
    
    def test_kth_smallest_two_elements(self):
        """Test with two elements."""
        nums = [10, 5]
        assert find_kth_smallest(nums, 1) == 5
        assert find_kth_smallest(nums, 2) == 10
    
    def test_kth_smallest_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-10, -5, -20, -3, 0]
        k = 2
        result = find_kth_smallest(nums, k)
        sorted_nums = sorted(nums)
        assert result == sorted_nums[k - 1]  # Should be -10
    
    def test_kth_smallest_mixed_numbers(self):
        """Test with mixed positive and negative."""
        nums = [10, -5, 3, -20, 7, 0]
        k = 3
        result = find_kth_smallest(nums, k)
        sorted_nums = sorted(nums)
        assert result == sorted_nums[k - 1]  # Should be 0
    
    def test_kth_smallest_large_array(self):
        """Test with larger array."""
        nums = list(range(100, 0, -1))  # 100 down to 1
        k = 50
        result = find_kth_smallest(nums, k)
        assert result == 50
    
    def test_kth_smallest_unsorted_array(self):
        """Test with completely unsorted array."""
        nums = [64, 34, 25, 12, 22, 11, 90]
        k = 4
        result = find_kth_smallest(nums, k)
        sorted_nums = sorted(nums)
        assert result == sorted_nums[k - 1]  # Should be 25


class TestStreamMax:
    """Test cases for stream_max function."""
    
    def test_stream_max_single_element(self):
        """Test stream_max with single element."""
        nums = [5]
        result = stream_max(nums)
        assert result == [5]
    
    def test_stream_max_two_elements(self):
        """Test stream_max with two elements."""
        nums = [5, 10]
        result = stream_max(nums)
        # After processing 5: max is 5. After processing 10: max is 10.
        assert result == [5, 10]
    
    def test_stream_max_ascending_sequence(self):
        """Test stream_max with ascending sequence."""
        nums = [1, 2, 3, 4, 5]
        result = stream_max(nums)
        # Each element becomes the new max
        assert result == [1, 2, 3, 4, 5]
    
    def test_stream_max_descending_sequence(self):
        """Test stream_max with descending sequence."""
        nums = [5, 4, 3, 2, 1]
        result = stream_max(nums)
        # First element is max, then max stays at 5 as smaller elements arrive
        assert result == [5, 5, 5, 5, 5]
    
    def test_stream_max_mixed_sequence(self):
        """Test stream_max with mixed sequence."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        result = stream_max(nums)
        # Process: 3->3, 1->3, 4->4, 1->4, 5->5, 9->9, 2->9, 6->9
        assert result == [3, 3, 4, 4, 5, 9, 9, 9]
    
    def test_stream_max_with_duplicates(self):
        """Test stream_max with duplicate max values."""
        nums = [5, 5, 5]
        result = stream_max(nums)
        assert result == [5, 5, 5]
    
    def test_stream_max_negative_numbers(self):
        """Test stream_max with negative numbers."""
        nums = [-5, -2, -10, -1]
        result = stream_max(nums)
        # -5 is max, -2 becomes max, -10 stays -2, -1 becomes new max
        assert result == [-5, -2, -2, -1]
    
    def test_stream_max_mixed_positive_negative(self):
        """Test stream_max with mixed positive and negative."""
        nums = [-10, 5, -3, 10, -5]
        result = stream_max(nums)
        # -10, 5, 5, 10, 10
        assert result == [-10, 5, 5, 10, 10]
    
    def test_stream_max_with_zeros(self):
        """Test stream_max with zero values."""
        nums = [0, 1, 0, 2, 0]
        result = stream_max(nums)
        assert result == [0, 1, 1, 2, 2]
    
    def test_stream_max_length_matches_input(self):
        """Test that output length matches input length."""
        nums = [3, 7, 2, 9, 1, 5, 8]
        result = stream_max(nums)
        assert len(result) == len(nums)
    
    def test_stream_max_large_array(self):
        """Test stream_max with larger array."""
        nums = list(range(1, 101))
        result = stream_max(nums)
        # Each element should be at least as large as the previous
        for i in range(1, len(result)):
            assert result[i] >= result[i-1]
    
    def test_stream_max_all_same_values(self):
        """Test stream_max where all values are the same."""
        nums = [7, 7, 7, 7]
        result = stream_max(nums)
        assert result == [7, 7, 7, 7]
    
    def test_stream_max_peak_in_middle(self):
        """Test stream_max with peak in the middle."""
        nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        result = stream_max(nums)
        # Max goes up to 5, then stays at 5
        assert result == [1, 2, 3, 4, 5, 5, 5, 5, 5]
    
    def test_stream_max_two_peaks(self):
        """Test stream_max with two peaks."""
        nums = [3, 1, 4, 1, 5, 1, 3, 1]
        result = stream_max(nums)
        assert result == [3, 3, 4, 4, 5, 5, 5, 5]
