import importlib.util
import pathlib


def _load_double_linked_list_module():
    module_path = pathlib.Path(__file__).with_name("intro.py")
    spec = importlib.util.spec_from_file_location("double_intro", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


intro = _load_double_linked_list_module()
DoubleLinkedList = intro.DoubleLinkedList
Node = intro.Node


def _values_forward(dll):
    values = []
    curr = dll.head
    while curr is not None:
        values.append(curr.value)
        curr = curr.next
    return values


def _values_backward(dll):
    values = []
    curr = dll.tail
    while curr is not None:
        values.append(curr.value)
        curr = curr.prev
    return values


def test_node_init_links():
    node = Node(7)
    assert node.value == 7
    assert node.next is None
    assert node.prev is None


def test_init_singleton():
    dll = DoubleLinkedList(1)
    assert dll.head is dll.tail
    assert dll.head.value == 1
    assert dll.tail.value == 1
    assert dll.length == 1
    assert dll.head.prev is None
    assert dll.head.next is None


def test_append_updates_links():
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)

    assert dll.length == 3
    assert dll.head.value == 1
    assert dll.tail.value == 3

    assert dll.head.next.value == 2
    assert dll.head.next.prev is dll.head
    assert dll.tail.prev.value == 2
    assert dll.tail.prev.next is dll.tail


def test_append_to_empty_head_none():
    dll = DoubleLinkedList(1)
    dll.head = None
    dll.tail = None
    dll.length = 0

    dll.append(10)

    assert dll.length == 1
    assert dll.head.value == 10
    assert dll.tail.value == 10
    assert dll.head is dll.tail
    assert dll.head.prev is None
    assert dll.head.next is None


def test_print_list_output(capsys):
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)

    dll.print_list()

    out = capsys.readouterr().out
    assert "The new list is" in out
    assert "1" in out
    assert "2" in out
    assert "3" in out
    assert "End of list" in out


def test_reverse_two_elements():
    dll = DoubleLinkedList(1)
    dll.append(2)

    dll.reverse()

    assert _values_forward(dll) == [2, 1]
    assert _values_backward(dll) == [1, 2]
    assert dll.head.value == 2
    assert dll.tail.value == 1
    assert dll.head.prev is None
    assert dll.tail.next is None


def test_reverse_multiple_elements():
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    dll.reverse()

    assert _values_forward(dll) == [4, 3, 2, 1]
    assert _values_backward(dll) == [1, 2, 3, 4]
    assert dll.head.value == 4
    assert dll.tail.value == 1

    # Internal links after reverse
    assert dll.head.next.value == 3
    assert dll.head.next.prev is dll.head
    assert dll.tail.prev.value == 2
    assert dll.tail.prev.next is dll.tail


def test_reverse_single_element():
    dll = DoubleLinkedList(1)

    dll.reverse()

    assert dll.head is dll.tail
    assert dll.head.value == 1
    assert dll.head.prev is None
    assert dll.head.next is None


def test_reverse_empty_list():
    dll = DoubleLinkedList(1)
    dll.head = None
    dll.tail = None
    dll.length = 0

    dll.reverse()

    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


def test_pop_single_and_empty():
    dll = DoubleLinkedList(1)

    node = dll.pop()

    assert node.value == 1
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0

    assert dll.pop() is None


def test_pop_multiple():
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)

    node = dll.pop()

    assert node.value == 3
    assert dll.length == 2
    assert dll.tail.value == 2
    assert dll.tail.next is None
    assert dll.head.prev is None


def test_prepend_to_empty():
    dll = DoubleLinkedList(1)
    dll.head = None
    dll.tail = None
    dll.length = 0

    dll.prepend(10)

    assert dll.length == 1
    assert dll.head.value == 10
    assert dll.tail.value == 10
    assert dll.head is dll.tail
    assert dll.head.prev is None
    assert dll.head.next is None


def test_prepend_to_nonempty():
    dll = DoubleLinkedList(2)
    dll.append(3)

    dll.prepend(1)

    assert dll.length == 3
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.next.prev is dll.head
    assert dll.tail.value == 3


def test_pop_first_single_and_multiple():
    dll = DoubleLinkedList(1)
    node = dll.pop_first()

    assert node.value == 1
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None

    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    node = dll.pop_first()

    assert node.value == 1
    assert dll.length == 2
    assert dll.head.value == 2
    assert dll.head.prev is None
    assert dll.tail.value == 3


def test_get_indices():
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)

    assert dll.get(0).value == 1
    assert dll.get(1).value == 2
    assert dll.get(2).value == 3
    assert dll.get(3) is None
    assert dll.get(-1) is None

    dll.head = None
    dll.tail = None
    dll.length = 0
    assert dll.get(0) is None


def test_set_updates_value():
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)

    assert dll.set(1, 20) is True
    assert dll.get(1).value == 20
    assert dll.set(3, 30) is False
    assert dll.set(-1, 30) is False


def test_insert_positions():
    dll = DoubleLinkedList(2)
    dll.append(4)

    assert dll.insert(0, 1) is True
    assert _values_forward(dll) == [1, 2, 4]
    assert dll.head.prev is None

    assert dll.insert(2, 3) is True
    assert _values_forward(dll) == [1, 2, 3, 4]
    assert dll.get(2).prev.value == 2
    assert dll.get(2).next.value == 4

    assert dll.insert(dll.length, 5) is True
    assert _values_forward(dll) == [1, 2, 3, 4, 5]
    assert dll.tail.value == 5
    assert dll.tail.next is None

    assert dll.insert(-1, 0) is False
    assert dll.insert(dll.length + 1, 6) is False


def test_remove_positions():
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    node = dll.remove(0)
    assert node.value == 1
    assert dll.head.value == 2
    assert dll.head.prev is None

    node = dll.remove(1)
    assert node.value == 3
    assert _values_forward(dll) == [2, 4]
    assert dll.head.next is dll.tail
    assert dll.tail.prev is dll.head

    node = dll.remove(dll.length - 1)
    assert node.value == 4
    assert dll.tail.value == 2
    assert dll.tail.next is None
    assert dll.length == 1

    assert dll.remove(5) is None
    assert dll.remove(-1) is None


# ============ Extended Edge Case Tests ============

def test_pop_until_empty():
    """Pop all elements one by one."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    
    assert dll.pop().value == 3
    assert dll.pop().value == 2
    assert dll.pop().value == 1
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None


def test_pop_preserves_backward_links():
    """Ensure pop maintains backward link integrity."""
    dll = DoubleLinkedList(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    
    popped = dll.pop()
    assert popped.value == 40
    
    assert dll.tail.prev is not None
    assert dll.tail.prev.value == 20
    assert dll.tail.prev.next is dll.tail
    assert _values_backward(dll) == [30, 20, 10]


def test_prepend_alternating_new_tail_updates():
    """Prepend maintains correct head after multiple operations."""
    dll = DoubleLinkedList(5)
    dll.prepend(4)
    dll.prepend(3)
    dll.prepend(2)
    dll.prepend(1)
    
    assert dll.head.value == 1
    assert dll.head.prev is None
    assert dll.head.next.value == 2
    assert _values_forward(dll) == [1, 2, 3, 4, 5]
    assert dll.length == 5


def test_prepend_changes_head_reference():
    """Ensure prepend updates head correctly."""
    dll = DoubleLinkedList(2)
    old_head = dll.head
    
    dll.prepend(1)
    
    assert dll.head != old_head
    assert dll.head.value == 1
    assert dll.head.next is old_head
    assert old_head.prev is dll.head


def test_pop_first_until_empty():
    """Pop first all elements one by one."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    
    node1 = dll.pop_first()
    assert node1.value == 1
    assert dll.head.value == 2
    assert dll.head.prev is None
    
    node2 = dll.pop_first()
    assert node2.value == 2
    assert dll.head.value == 3
    assert dll.head is dll.tail
    
    node3 = dll.pop_first()
    assert node3.value == 3
    assert dll.pop_first() is None


def test_pop_first_maintains_backward_links():
    """Pop_first preserves backward link structure."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    
    dll.pop_first()
    dll.pop_first()
    
    assert _values_backward(dll) == [4, 3]
    assert dll.head.prev is None


def test_get_after_pop_operations():
    """Get correctly indexes after popping."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    
    dll.pop()
    dll.pop_first()
    
    assert dll.get(0).value == 2
    assert dll.get(1).value == 3
    assert dll.get(2) is None
    assert dll.length == 2


def test_get_returns_node_object():
    """Get returns actual node, not copy."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    
    node = dll.get(1)
    assert node is dll.head.next
    assert node.prev is dll.head
    assert node.next is dll.tail


def test_set_with_all_positions():
    """Set works at all valid indices."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    
    for i in range(dll.length):
        assert dll.set(i, i * 10) is True
    
    assert _values_forward(dll) == [0, 10, 20, 30, 40]


def test_set_at_boundaries():
    """Set at head and tail updates correctly."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    
    dll.set(0, 100)
    assert dll.head.value == 100
    
    dll.set(dll.length - 1, 300)
    assert dll.tail.value == 300


def test_insert_at_boundaries():
    """Insert at zero and at length."""
    dll = DoubleLinkedList(2)
    dll.append(3)
    
    dll.insert(0, 1)
    assert dll.head.value == 1
    
    dll.insert(dll.length, 4)
    assert dll.tail.value == 4
    
    assert _values_forward(dll) == [1, 2, 3, 4]


def test_insert_builds_list():
    """Build list entirely through inserts."""
    dll = DoubleLinkedList(1)
    
    dll.insert(1, 3)
    dll.insert(1, 2)
    dll.insert(3, 4)
    
    assert _values_forward(dll) == [1, 2, 3, 4]
    assert dll.length == 4


def test_insert_maintains_links():
    """Insert maintains backward and forward links."""
    dll = DoubleLinkedList(1)
    dll.append(3)
    
    dll.insert(1, 2)
    
    node2 = dll.get(1)
    assert node2.value == 2
    assert node2.prev is dll.head
    assert node2.next is dll.tail
    assert dll.head.next is node2
    assert dll.tail.prev is node2


def test_remove_from_middle_restores_links():
    """Remove from middle maintains full link integrity."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    
    dll.remove(1)
    
    assert dll.head.next is dll.get(1)
    assert dll.get(1).prev is dll.head
    assert _values_forward(dll) == [1, 3, 4]
    assert _values_backward(dll) == [4, 3, 1]


def test_remove_until_singleton():
    """Remove elements until one remains."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    
    while dll.length > 1:
        dll.remove(0)
    
    assert dll.length == 1
    assert dll.head is dll.tail
    assert dll.head.prev is None
    assert dll.head.next is None


def test_sequential_operations_mixed():
    """Chain multiple operations and verify integrity."""
    dll = DoubleLinkedList(2)
    dll.append(5)
    dll.prepend(1)
    dll.insert(2, 3)
    dll.insert(3, 4)
    
    assert _values_forward(dll) == [1, 2, 3, 4, 5]
    
    dll.pop()
    dll.pop_first()
    
    assert _values_forward(dll) == [2, 3, 4]
    assert _values_backward(dll) == [4, 3, 2]


def test_all_methods_maintain_length():
    """Length tracks correctly through all operations."""
    dll = DoubleLinkedList(1)
    assert dll.length == 1
    
    dll.append(2)
    assert dll.length == 2
    
    dll.prepend(0)
    assert dll.length == 3
    
    dll.insert(1, 0.5)
    assert dll.length == 4
    
    dll.pop()
    assert dll.length == 3
    
    dll.pop_first()
    assert dll.length == 2
    
    dll.remove(0)
    assert dll.length == 1

def test_is_palindrome_single_element():
    """Single element list is a palindrome."""
    dll = DoubleLinkedList(1)
    assert dll.is_palindrome() is True


def test_is_palindrome_two_identical_elements():
    """Two identical elements form a palindrome."""
    dll = DoubleLinkedList(5)
    dll.append(5)
    assert dll.is_palindrome() is True


def test_is_palindrome_two_different_elements():
    """Two different elements do not form a palindrome."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    assert dll.is_palindrome() is False


def test_is_palindrome_odd_length_palindrome():
    """Odd length palindrome: 1-2-1."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(1)
    assert dll.is_palindrome() is True


def test_is_palindrome_odd_length_non_palindrome():
    """Odd length non-palindrome: 1-2-3."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    assert dll.is_palindrome() is False


def test_is_palindrome_even_length_palindrome():
    """Even length palindrome: 1-2-2-1."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(2)
    dll.append(1)
    assert dll.is_palindrome() is True


def test_is_palindrome_even_length_non_palindrome():
    """Even length non-palindrome: 1-2-3-4."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    assert dll.is_palindrome() is False


def test_is_palindrome_longer_palindrome():
    """Longer palindrome: 1-2-3-2-1."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(2)
    dll.append(1)
    assert dll.is_palindrome() is True


def test_is_palindrome_longer_even_palindrome():
    """Longer even length palindrome: 1-2-3-3-2-1."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(3)
    dll.append(2)
    dll.append(1)
    assert dll.is_palindrome() is True


def test_is_palindrome_all_same_elements():
    """All same elements form a palindrome."""
    dll = DoubleLinkedList(7)
    dll.append(7)
    dll.append(7)
    dll.append(7)
    assert dll.is_palindrome() is True


def test_is_palindrome_string_values():
    """Palindrome with string values: a-b-a."""
    dll = DoubleLinkedList("a")
    dll.append("b")
    dll.append("a")
    assert dll.is_palindrome() is True


def test_is_palindrome_string_non_palindrome():
    """Non-palindrome with string values: a-b-c."""
    dll = DoubleLinkedList("a")
    dll.append("b")
    dll.append("c")
    assert dll.is_palindrome() is False


def test_is_palindrome_complex_palindrome():
    """Complex palindrome: 10-20-30-20-10."""
    dll = DoubleLinkedList(10)
    dll.append(20)
    dll.append(30)
    dll.append(20)
    dll.append(10)
    assert dll.is_palindrome() is True


# ===================== make_empty tests =====================

def test_make_empty_single_element():
    """Make empty on single element list."""
    dll = DoubleLinkedList(1)
    dll.make_empty()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


def test_make_empty_multiple_elements():
    """Make empty on list with multiple elements."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.make_empty()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


def test_make_empty_then_append():
    """After make_empty, list can be used again."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.make_empty()
    dll.append(10)
    assert dll.head.value == 10
    assert dll.tail.value == 10
    assert dll.length == 1
    assert dll.head is dll.tail


def test_make_empty_idempotent():
    """Calling make_empty twice should be safe."""
    dll = DoubleLinkedList(1)
    dll.make_empty()
    dll.make_empty()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


# ===================== partition_list tests =====================

def test_partition_list_basic():
    """Partition list: elements < x come before elements >= x."""
    dll = DoubleLinkedList(3)
    dll.append(5)
    dll.append(8)
    dll.append(5)
    dll.append(10)
    dll.append(2)
    dll.append(1)
    
    dll.partition_list(5)
    
    values = _values_forward(dll)
    # All elements < 5 should come first: [3, 2, 1]
    # All elements >= 5 should come after: [5, 8, 5, 10]
    assert values == [3, 2, 1, 5, 8, 5, 10]


def test_partition_list_all_less_than_x():
    """All elements less than x."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    
    dll.partition_list(10)
    
    assert _values_forward(dll) == [1, 2, 3]
    assert _values_backward(dll) == [3, 2, 1]


def test_partition_list_all_greater_or_equal():
    """All elements greater than or equal to x."""
    dll = DoubleLinkedList(5)
    dll.append(6)
    dll.append(7)
    
    dll.partition_list(2)
    
    assert _values_forward(dll) == [5, 6, 7]
    assert _values_backward(dll) == [7, 6, 5]


def test_partition_list_single_element_less():
    """Single element less than x."""
    dll = DoubleLinkedList(1)
    
    dll.partition_list(5)
    
    assert _values_forward(dll) == [1]
    assert dll.head is dll.tail


def test_partition_list_single_element_greater_or_equal():
    """Single element greater than or equal to x."""
    dll = DoubleLinkedList(5)
    
    dll.partition_list(3)
    
    assert _values_forward(dll) == [5]
    assert dll.head is dll.tail


def test_partition_list_preserves_relative_order():
    """Relative order within partitions is preserved."""
    dll = DoubleLinkedList(1)
    dll.append(4)
    dll.append(3)
    dll.append(2)
    dll.append(5)
    dll.append(2)
    
    dll.partition_list(3)
    
    values = _values_forward(dll)
    # Elements < 3: [1, 2, 2] in original relative order
    # Elements >= 3: [4, 3, 5] in original relative order
    assert values == [1, 2, 2, 4, 3, 5]


def test_partition_list_bidirectional_links():
    """After partition, prev/next links are correct."""
    dll = DoubleLinkedList(3)
    dll.append(1)
    dll.append(4)
    dll.append(2)
    
    dll.partition_list(3)
    
    # Expected: [1, 2, 3, 4]
    assert _values_forward(dll) == [1, 2, 3, 4]
    assert _values_backward(dll) == [4, 3, 2, 1]
    assert dll.head.prev is None
    assert dll.tail.next is None


def test_partition_list_length_preserved():
    """Length is preserved after partition."""
    dll = DoubleLinkedList(3)
    dll.append(1)
    dll.append(4)
    dll.append(2)
    original_length = dll.length
    
    dll.partition_list(3)
    
    assert dll.length == original_length


# ===================== partition_list_dummy_nodes tests =====================

def test_partition_list_dummy_nodes_basic():
    """Partition list (dummy nodes): elements < x come before elements >= x."""
    dll = DoubleLinkedList(3)
    dll.append(5)
    dll.append(8)
    dll.append(5)
    dll.append(10)
    dll.append(2)
    dll.append(1)
    dll.partition_list_dummy_nodes(5)
    values = _values_forward(dll)
    assert values == [3, 2, 1, 5, 8, 5, 10]

def test_partition_list_dummy_nodes_all_less_than_x():
    """All elements less than x (dummy nodes)."""
    dll = DoubleLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.partition_list_dummy_nodes(10)
    assert _values_forward(dll) == [1, 2, 3]
    assert _values_backward(dll) == [3, 2, 1]

def test_partition_list_dummy_nodes_all_greater_or_equal():
    """All elements greater than or equal to x (dummy nodes)."""
    dll = DoubleLinkedList(5)
    dll.append(6)
    dll.append(7)
    dll.partition_list_dummy_nodes(2)
    assert _values_forward(dll) == [5, 6, 7]
    assert _values_backward(dll) == [7, 6, 5]

def test_partition_list_dummy_nodes_single_element_less():
    """Single element less than x (dummy nodes)."""
    dll = DoubleLinkedList(1)
    dll.partition_list_dummy_nodes(5)
    assert _values_forward(dll) == [1]
    assert dll.head is dll.tail

def test_partition_list_dummy_nodes_single_element_greater_or_equal():
    """Single element greater than or equal to x (dummy nodes)."""
    dll = DoubleLinkedList(5)
    dll.partition_list_dummy_nodes(3)
    assert _values_forward(dll) == [5]
    assert dll.head is dll.tail

def test_partition_list_dummy_nodes_preserves_relative_order():
    """Relative order within partitions is preserved (dummy nodes)."""
    dll = DoubleLinkedList(1)
    dll.append(4)
    dll.append(3)
    dll.append(2)
    dll.append(5)
    dll.append(2)
    dll.partition_list_dummy_nodes(3)
    values = _values_forward(dll)
    assert values == [1, 2, 2, 4, 3, 5]

def test_partition_list_dummy_nodes_bidirectional_links():
    """After partition (dummy nodes), prev/next links are correct."""
    dll = DoubleLinkedList(3)
    dll.append(1)
    dll.append(4)
    dll.append(2)
    dll.partition_list_dummy_nodes(3)
    assert _values_forward(dll) == [1, 2, 3, 4]
    assert _values_backward(dll) == [4, 3, 2, 1]
    assert dll.head.prev is None
    assert dll.tail.next is None

def test_partition_list_dummy_nodes_length_preserved():
    """Length is preserved after partition (dummy nodes)."""
    dll = DoubleLinkedList(3)
    dll.append(1)
    dll.append(4)
    dll.append(2)
    original_length = dll.length
    dll.partition_list_dummy_nodes(3)
    assert dll.length == original_length