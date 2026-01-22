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
    # pop_clean on non-empty single should return value and make list empty
    v = ll.pop_clean()
    assert v == 100
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
    assert x == 7
    assert ll.length == 1
    assert ll.head.value == 8
    # pop_first until empty
    assert ll.pop_first() == 8
    assert ll.pop_first() is None


def test_print_list_output(capsys):
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()
    captured = capsys.readouterr()
    out = captured.out
    assert "The new list is" in out
    assert "End of list" in out
    assert "1" in out
    assert "2" in out
    assert "3" in out


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
    assert val == 4
    assert ll.length == 3
    assert ll.tail.value == 3
    assert ll.tail.next is None  # Verify tail.next is disconnected

    # Pop another element (3) - now this works correctly
    val = ll.pop_clean()
    assert val == 3
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
    assert val == 10
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
