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
    """Test get method retrieves the first element at index 0."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    assert ll.get(0) == 10


def test_get_last_element():
    """Test get method retrieves the last element."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    assert ll.get(2) == 30


def test_get_middle_element():
    """Test get method retrieves a middle element."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    assert ll.get(1) == 20
    assert ll.get(2) == 30


def test_get_single_element_list():
    """Test get on a single-element list at index 0."""
    ll = LinkedList(42)
    assert ll.get(0) == 42


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
    assert ll.get(2) == 15  # Valid last index
    assert ll.get(3) is None  # Out of bounds


def test_get_after_modifications():
    """Test get works correctly after list modifications."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)

    # Get before modification
    assert ll.get(1) == 2

    # Pop and verify get still works
    ll.pop()
    assert ll.get(1) == 2
    assert ll.get(2) is None  # No longer exists

    # Prepend and verify indices shifted
    ll.prepend(0)
    assert ll.get(0) == 0
    assert ll.get(1) == 1
    assert ll.get(2) == 2
