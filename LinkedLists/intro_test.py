import pytest
from intro import LinkedList, Node


def test_init():
    ll = LinkedList(1)
    assert ll.head is not None
    assert ll.tail is not None
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.length == 1


def test_append_and_tail():
    ll = LinkedList(1)
    ll.append(2)
    assert ll.length == 2
    assert ll.tail.value == 2
    assert ll.head.next.value == 2


def test_pop_single_and_empty():
    ll = LinkedList(42)
    val = ll.pop()
    assert val == 42
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0
    # popping empty returns None
    assert ll.pop() is None


def test_pop_multiple():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    assert ll.length == 3
    val = ll.pop()
    assert val == 3
    assert ll.length == 2
    assert ll.tail.value == 2


def test_pop_clean_empty_and_single():
    ll = LinkedList(100)
    # pop_clean on non-empty single should return node and make list empty
    v = ll.pop_clean()
    assert v.value == 100
    assert ll.length == 0
    assert ll.head is None and ll.tail is None
    # pop_clean on empty returns None
    assert ll.pop_clean() is None


def test_prepend_after_empty_and_nonempty():
    ll = LinkedList(5)
    ll.pop()
    assert ll.length == 0
    ll.prepend(10)
    assert ll.length == 1
    assert ll.head.value == 10
    assert ll.tail.value == 10

    ll.prepend(20)
    assert ll.length == 2
    assert ll.head.value == 20
    assert ll.head.next.value == 10


def test_pop_first_behaviour():
    ll = LinkedList(7)
    ll.append(8)
    x = ll.pop_first()
    assert x.value == 7
    assert ll.length == 1
    assert ll.head.value == 8
    # pop_first until empty
    node = ll.pop_first()
    assert node.value == 8
    assert ll.pop_first() is None


def test_print_list_output(capsys):
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()
    captured = capsys.readouterr()
    out = captured.out
    assert "1 -> 2 -> 3 -> None" in out
    assert "->" in out


def test_print_empty_list(capsys):
    """Test printing an empty list."""
    ll = LinkedList(1)
    ll.pop()
    ll.print_list()
    captured = capsys.readouterr()
    out = captured.out
    assert out.strip() == "None"


def test_print_single_element(capsys):
    """Test printing a single element list."""
    ll = LinkedList(42)
    ll.print_list()
    captured = capsys.readouterr()
    out = captured.out
    assert "42 -> None" in out


# --- New tests for improved coverage ---


def test_append_to_empty_list():
    """Test appending to an empty list (covers lines 24-25 in append method)."""
    ll = LinkedList(1)
    # Pop the single element to make the list empty
    ll.pop()
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0

    # Now append to the empty list - this tests the if self.head is None branch
    ll.append(42)
    assert ll.head is not None
    assert ll.tail is not None
    assert ll.head.value == 42
    assert ll.tail.value == 42
    assert ll.length == 1


def test_pop_clean_with_multiple_elements():
    """Test pop_clean with 3+ elements to verify it removes the last element."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    assert ll.length == 4

    # Pop the last element (4)
    val = ll.pop_clean()
    assert val.value == 4
    assert ll.length == 3
    assert ll.tail.value == 3
    assert ll.tail.next is None  # Verify tail.next is disconnected

    # Pop another element (3) - now this works correctly
    val = ll.pop_clean()
    assert val.value == 3
    assert ll.length == 2
    assert ll.tail.value == 2
    assert ll.tail.next is None


def test_pop_first_two_to_one_element():
    """Test pop_first when reducing a 2-element list to 1 element."""
    ll = LinkedList(10)
    ll.append(20)
    assert ll.length == 2
    assert ll.head.value == 10
    assert ll.tail.value == 20

    # Pop first element, leaving only one
    val = ll.pop_first()
    assert val.value == 10
    assert ll.length == 1
    assert ll.head.value == 20
    # Note: tail still points to the remaining element
    assert ll.tail.value == 20


def test_node_class_directly():
    """Test Node initialization to ensure value and next are set correctly."""
    node = Node(99)
    assert node.value == 99
    assert node.next is None

    # Test linking nodes manually
    node2 = Node(100)
    node.next = node2
    assert node.next is node2
    assert node.next.value == 100


# --- Tests for get method ---


def test_get_first_element():
    """Test get method retrieves the first Node at index 0."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    node = ll.get(0)
    assert node is not None
    assert node.value == 10
    assert node is ll.head


def test_get_last_element():
    """Test get method retrieves the last Node."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    node = ll.get(2)
    assert node is not None
    assert node.value == 30
    assert node is ll.tail


def test_get_middle_element():
    """Test get method retrieves a middle Node."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    node = ll.get(1)
    assert node is not None
    assert node.value == 20
    
    node = ll.get(2)
    assert node is not None
    assert node.value == 30


def test_get_single_element_list():
    """Test get on a single-element list at index 0."""
    ll = LinkedList(42)
    node = ll.get(0)
    assert node is not None
    assert node.value == 42
    assert node is ll.head
    assert node is ll.tail


def test_get_negative_index():
    """Test get returns None for negative index."""
    ll = LinkedList(10)
    ll.append(20)
    assert ll.get(-1) is None
    assert ll.get(-10) is None


def test_get_index_out_of_bounds():
    """Test get returns None for index >= length."""
    ll = LinkedList(10)
    ll.append(20)
    assert ll.length == 2
    assert ll.get(2) is None
    assert ll.get(3) is None
    assert ll.get(100) is None


def test_get_empty_list():
    """Test get returns None for an empty list."""
    ll = LinkedList(1)
    ll.pop()  # Make it empty
    assert ll.length == 0
    assert ll.get(0) is None
    assert ll.get(1) is None


def test_get_boundary_index():
    """Test get at boundary index (length - 1)."""
    ll = LinkedList(5)
    ll.append(10)
    ll.append(15)
    # length is 3, so valid indices are 0, 1, 2
    node = ll.get(2)  # Valid last index
    assert node is not None
    assert node.value == 15
    assert ll.get(3) is None  # Out of bounds


def test_get_after_modifications():
    """Test get works correctly after list modifications."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)

    # Get before modification
    node = ll.get(1)
    assert node is not None
    assert node.value == 2

    # Pop and verify get still works
    ll.pop()
    node = ll.get(1)
    assert node is not None
    assert node.value == 2
    assert ll.get(2) is None  # No longer exists

    # Prepend and verify indices shifted
    ll.prepend(0)
    node = ll.get(0)
    assert node is not None
    assert node.value == 0
    assert ll.get(1).value == 1
    assert ll.get(2).value == 2

# --- Tests for set_value method ---


def test_set_value_first_element():
    """Test set_value changes the first element (index 0)."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    result = ll.set_value(0, 100)
    assert result is True
    assert ll.get(0).value == 100
    assert ll.head.value == 100


def test_set_value_last_element():
    """Test set_value changes the last element."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    result = ll.set_value(2, 300)
    assert result is True
    assert ll.get(2).value == 300
    assert ll.tail.value == 300


def test_set_value_middle_element():
    """Test set_value changes a middle element."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    
    result = ll.set_value(1, 200)
    assert result is True
    assert ll.get(1).value == 200
    assert ll.get(0).value == 10  # Verify others unchanged
    assert ll.get(2).value == 30
    assert ll.get(3).value == 40


def test_set_value_single_element_list():
    """Test set_value on a single-element list."""
    ll = LinkedList(42)
    
    result = ll.set_value(0, 99)
    assert result is True
    assert ll.get(0).value == 99
    assert ll.head.value == 99
    assert ll.tail.value == 99


def test_set_value_negative_index():
    """Test set_value returns False for negative index."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.set_value(-1, 100)
    assert result is False
    assert ll.get(0).value == 10  # Value should remain unchanged
    assert ll.get(1).value == 20


def test_set_value_index_out_of_bounds():
    """Test set_value returns False for index >= length."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    assert ll.length == 3
    
    # Test index equal to length
    result = ll.set_value(3, 999)
    assert result is False
    
    # Test index greater than length
    result = ll.set_value(10, 999)
    assert result is False
    
    # Verify no values changed
    assert ll.get(0).value == 10
    assert ll.get(1).value == 20
    assert ll.get(2).value == 30


def test_set_value_empty_list():
    """Test set_value returns False on an empty list."""
    ll = LinkedList(1)
    ll.pop()  # Make it empty
    
    assert ll.length == 0
    
    result = ll.set_value(0, 100)
    assert result is False


def test_set_value_with_zero():
    """Test set_value can set a value to zero."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.set_value(0, 0)
    assert result is True
    assert ll.get(0).value == 0


def test_set_value_with_negative_value():
    """Test set_value can set a value to a negative number."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.set_value(1, -50)
    assert result is True
    assert ll.get(1).value == -50


def test_set_value_with_string():
    """Test set_value can set string values."""
    ll = LinkedList("hello")
    ll.append("world")
    
    result = ll.set_value(0, "goodbye")
    assert result is True
    assert ll.get(0).value == "goodbye"
    
    result = ll.set_value(1, "universe")
    assert result is True
    assert ll.get(1).value == "universe"


def test_set_value_multiple_operations():
    """Test multiple set_value operations on the same list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    # First set
    assert ll.set_value(0, 10) is True
    assert ll.get(0).value == 10
    
    # Second set on different index
    assert ll.set_value(2, 30) is True
    assert ll.get(2).value == 30
    
    # Third set on same index
    assert ll.set_value(1, 200) is True
    assert ll.get(1).value == 200
    
    # Verify all values
    assert ll.get(0).value == 10
    assert ll.get(1).value == 200
    assert ll.get(2).value == 30
    assert ll.get(3).value == 4


def test_set_value_boundary_indices():
    """Test set_value at boundary indices (0 and length-1)."""
    ll = LinkedList(5)
    ll.append(10)
    ll.append(15)
    
    # Set at index 0 (first element)
    assert ll.set_value(0, 50) is True
    assert ll.get(0).value == 50
    
    # Set at index length-1 (last element, index 2)
    assert ll.set_value(2, 150) is True
    assert ll.get(2).value == 150
    
    # Try to set at index length (out of bounds)
    assert ll.set_value(3, 999) is False

# --- Tests for insert method ---


def test_insert_at_beginning():
    """Test insert at index 0 (beginning of list)."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    result = ll.insert(0, 5)
    assert result is True
    assert ll.length == 4
    assert ll.head.value == 5
    assert ll.get(0).value == 5
    assert ll.get(1).value == 10
    assert ll.get(2).value == 20
    assert ll.get(3).value == 30


def test_insert_in_middle():
    """Test insert in the middle of the list."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(40)
    
    result = ll.insert(2, 30)
    assert result is True
    assert ll.length == 4
    assert ll.get(0).value == 10
    assert ll.get(1).value == 20
    assert ll.get(2).value == 30
    assert ll.get(3).value == 40


def test_insert_at_end():
    """Test insert at the end (at index equal to length)."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    result = ll.insert(3, 40)
    assert result is True
    assert ll.length == 4
    assert ll.get(3).value == 40


def test_insert_single_element_at_beginning():
    """Test insert at beginning of single-element list."""
    ll = LinkedList(10)
    
    result = ll.insert(0, 5)
    assert result is True
    assert ll.length == 2
    assert ll.head.value == 5
    assert ll.get(0).value == 5
    assert ll.get(1).value == 10


def test_insert_single_element_at_end():
    """Test insert at end of single-element list."""
    ll = LinkedList(10)
    
    result = ll.insert(1, 20)
    assert result is True
    assert ll.length == 2
    assert ll.get(0).value == 10
    assert ll.get(1).value == 20


def test_insert_negative_index():
    """Test insert with negative index returns False."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.insert(-1, 5)
    assert result is False
    assert ll.length == 2
    assert ll.get(0).value == 10
    assert ll.get(1).value == 20


def test_insert_index_beyond_length():
    """Test insert with index beyond length returns False."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.insert(5, 100)
    assert result is False
    assert ll.length == 2


def test_insert_multiple_values():
    """Test multiple consecutive inserts."""
    ll = LinkedList(10)
    ll.append(40)
    
    assert ll.insert(1, 20) is True
    assert ll.length == 3
    
    assert ll.insert(2, 30) is True
    assert ll.length == 4
    
    assert ll.get(0).value == 10
    assert ll.get(1).value == 20
    assert ll.get(2).value == 30
    assert ll.get(3).value == 40


def test_insert_with_zero_value():
    """Test insert with zero as value."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.insert(1, 0)
    assert result is True
    assert ll.length == 3
    assert ll.get(1).value == 0


def test_insert_with_negative_value():
    """Test insert with negative number as value."""
    ll = LinkedList(10)
    ll.append(20)
    
    result = ll.insert(1, -5)
    assert result is True
    assert ll.length == 3
    assert ll.get(1).value == -5


def test_insert_with_string():
    """Test insert with string values."""
    ll = LinkedList("a")
    ll.append("c")
    
    result = ll.insert(1, "b")
    assert result is True
    assert ll.length == 3
    assert ll.get(0).value == "a"
    assert ll.get(1).value == "b"
    assert ll.get(2).value == "c"


def test_insert_building_list():
    """Test building a list using multiple inserts at index 0."""
    ll = LinkedList(1)
    
    assert ll.insert(0, 2) is True
    assert ll.insert(0, 3) is True
    assert ll.insert(0, 4) is True
    
    assert ll.length == 4
    assert ll.get(0).value == 4
    assert ll.get(1).value == 3
    assert ll.get(2).value == 2
    assert ll.get(3).value == 1


def test_insert_preserves_links():
    """Test that insert properly maintains node links."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    result = ll.insert(1, 15)
    assert result is True
    
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    
    assert values == [10, 15, 20, 30]


def test_insert_at_each_position():
    """Test inserting at every valid position."""
    ll = LinkedList(1)
    ll.append(3)
    
    assert ll.insert(1, 2) is True
    assert ll.length == 3
    
    ll2 = LinkedList(5)
    assert ll2.insert(0, 1) is True
    assert ll2.insert(1, 2) is True
    assert ll2.insert(2, 3) is True
    assert ll2.insert(3, 4) is True
    
    assert ll2.length == 5
    for i in range(5):
        assert ll2.get(i).value == i + 1


# --- Tests for remove method ---


def test_remove_from_beginning():
    """Test removing the first element from a list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    removed = ll.remove(0)
    assert removed.value == 1
    assert ll.length == 2
    assert ll.head.value == 2


def test_remove_from_end():
    """Test removing the last element from a list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    removed = ll.remove(2)
    assert removed.value == 3
    assert ll.length == 2
    assert ll.tail.value == 2


def test_remove_from_middle():
    """Test removing an element from the middle of the list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    removed = ll.remove(2)
    assert removed.value == 3
    assert ll.length == 3
    assert ll.get(0).value == 1
    assert ll.get(1).value == 2
    assert ll.get(2).value == 4


def test_remove_single_element():
    """Test removing the only element in the list."""
    ll = LinkedList(42)
    
    removed = ll.remove(0)
    assert removed.value == 42
    assert ll.length == 0
    assert ll.head is None
    assert ll.tail is None


def test_remove_negative_index():
    """Test that removing with a negative index returns None."""
    ll = LinkedList(1)
    ll.append(2)
    
    result = ll.remove(-1)
    assert result is None
    assert ll.length == 2


def test_remove_index_out_of_bounds():
    """Test that removing with an out-of-bounds index returns None."""
    ll = LinkedList(1)
    ll.append(2)
    
    result = ll.remove(5)
    assert result is None
    assert ll.length == 2
    
    result = ll.remove(2)
    assert result is None
    assert ll.length == 2


def test_remove_from_empty_list():
    """Test that removing from an empty list returns None."""
    ll = LinkedList(1)
    ll.pop()
    
    result = ll.remove(0)
    assert result is None


def test_remove_preserves_links():
    """Test that remove properly maintains node links."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    
    ll.remove(2)
    
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    
    assert values == [10, 20, 40, 50]
    assert ll.length == 4


def test_remove_multiple_sequential():
    """Test removing multiple elements sequentially."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    assert ll.remove(1).value == 2
    assert ll.length == 4
    assert ll.remove(1).value == 3
    assert ll.length == 3
    assert ll.remove(1).value == 4
    assert ll.length == 2
    
    assert ll.get(0).value == 1
    assert ll.get(1).value == 5


def test_remove_returned_node_isolated():
    """Test that the removed node has its next pointer set to None."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    removed = ll.remove(1)
    assert removed.value == 2
    assert removed.next is None


def test_remove_all_elements():
    """Test removing all elements from the list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    ll.remove(2)
    ll.remove(1)
    ll.remove(0)
    
    assert ll.length == 0
    assert ll.head is None
    assert ll.tail is None


def test_remove_boundary_indices():
    """Test removing at boundary indices (0 and length-1)."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    
    first = ll.remove(0)
    assert first.value == 10
    assert ll.head.value == 20
    
    last = ll.remove(2)
    assert last.value == 40
    assert ll.tail.value == 30


def test_remove_updates_length():
    """Test that remove properly decrements the length."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    initial_length = ll.length
    ll.remove(2)
    assert ll.length == initial_length - 1
    
    ll.remove(1)
    assert ll.length == initial_length - 2


# --- Tests for reverse method ---


def test_reverse_empty_list():
    """Test reversing an empty list."""
    ll = LinkedList(1)
    ll.pop()
    
    result = ll.reverse()
    assert result is True
    assert ll.length == 0


def test_reverse_single_element():
    """Test reversing a list with a single element."""
    ll = LinkedList(42)
    
    result = ll.reverse()
    assert result is True
    assert ll.head.value == 42
    assert ll.tail.value == 42
    assert ll.length == 1


def test_reverse_two_elements():
    """Test reversing a list with two elements."""
    ll = LinkedList(1)
    ll.append(2)
    
    result = ll.reverse()
    assert result is True
    assert ll.head.value == 2
    assert ll.tail.value == 1
    assert ll.length == 2
    assert ll.head.next.value == 1
    assert ll.tail.next is None


def test_reverse_three_elements():
    """Test reversing a list with three elements."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    result = ll.reverse()
    assert result is True
    assert ll.head.value == 3
    assert ll.tail.value == 1
    assert ll.length == 3
    
    # Verify the order
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    assert values == [3, 2, 1]


def test_reverse_multiple_elements():
    """Test reversing a list with multiple elements."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    result = ll.reverse()
    assert result is True
    assert ll.head.value == 5
    assert ll.tail.value == 1
    assert ll.length == 5
    
    # Verify the complete reversed order
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    assert values == [5, 4, 3, 2, 1]


def test_reverse_twice():
    """Test that reversing twice returns to original order."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    # First reverse
    ll.reverse()
    node = ll.head
    values_first = []
    while node:
        values_first.append(node.value)
        node = node.next
    assert values_first == [4, 3, 2, 1]
    
    # Second reverse
    ll.reverse()
    node = ll.head
    values_second = []
    while node:
        values_second.append(node.value)
        node = node.next
    assert values_second == [1, 2, 3, 4]


def test_reverse_preserves_length():
    """Test that reverse preserves the length of the list."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    
    original_length = ll.length
    ll.reverse()
    assert ll.length == original_length


def test_reverse_with_duplicate_values():
    """Test reversing a list with duplicate values."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(1)
    
    ll.reverse()
    
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    assert values == [1, 3, 2, 2, 1]


def test_reverse_all_links_correct():
    """Test that all node links are correctly updated after reverse."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    ll.reverse()
    
    # Check head to tail traversal
    assert ll.head.value == 4
    assert ll.head.next.value == 3
    assert ll.head.next.next.value == 2
    assert ll.head.next.next.next.value == 1
    assert ll.head.next.next.next.next is None
    
    # Check tail
    assert ll.tail.value == 1
    assert ll.tail.next is None


def test_reverse_head_tail_swap():
    """Test that head and tail are swapped after reverse."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    
    original_head = ll.head.value
    original_tail = ll.tail.value
    
    ll.reverse()
    
    assert ll.head.value == original_tail
    assert ll.tail.value == original_head


def test_reverse_after_operations():
    """Test reversing after various list operations."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    ll.remove(2)  # Remove 3
    ll.prepend(0)
    
    ll.reverse()
    
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    assert values == [5, 4, 2, 1, 0]


def test_reverse_large_list():
    """Test reversing a larger list."""
    ll = LinkedList(1)
    for i in range(2, 11):
        ll.append(i)
    
    ll.reverse()
    
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    
    assert values == list(range(10, 0, -1))
    assert ll.length == 10


def test_reverse_with_strings():
    """Test reversing a list with string values."""
    ll = LinkedList("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    
    ll.reverse()
    
    node = ll.head
    values = []
    while node:
        values.append(node.value)
        node = node.next
    
    assert values == ["d", "c", "b", "a"]
