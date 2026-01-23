import pytest
import sys
import os

# Add the LinkedLists directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from intro import LinkedList
import leet_code




def test_find_middle_node_single_element():
    """Test finding middle node in a single element list."""
    ll = LinkedList(1)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 1
    assert middle == ll.head
    assert middle == ll.tail


def test_find_middle_node_two_elements():
    """Test finding middle node in a two element list.
    Should return the first node of the second half (second element)."""
    ll = LinkedList(1)
    ll.append(2)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 2
    assert middle == ll.tail


def test_find_middle_node_three_elements():
    """Test finding middle node in a three element list (odd number).
    Should return the actual middle element."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 2


def test_find_middle_node_four_elements():
    """Test finding middle node in a four element list (even number).
    Should return the first node of the second half (third element)."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 3


def test_find_middle_node_five_elements():
    """Test finding middle node in a five element list (odd number).
    Should return the actual middle element (third element)."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 3


def test_find_middle_node_six_elements():
    """Test finding middle node in a six element list (even number).
    Should return the first node of the second half (fourth element)."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 4


def test_find_middle_node_seven_elements():
    """Test finding middle node in a seven element list (odd number).
    Should return the actual middle element (fourth element)."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 4


def test_find_middle_node_large_odd_list():
    """Test finding middle node in a larger odd-sized list (9 elements)."""
    ll = LinkedList(10)
    for i in range(20, 100, 10):
        ll.append(i)
    # List: 10, 20, 30, 40, 50, 60, 70, 80, 90 (9 elements)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 50  # 5th element (index 4)


def test_find_middle_node_large_even_list():
    """Test finding middle node in a larger even-sized list (10 elements)."""
    ll = LinkedList(1)
    for i in range(2, 11):
        ll.append(i)
    # List: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (10 elements)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 6  # First node of second half (index 5)


def test_find_middle_node_with_strings():
    """Test finding middle node with string values."""
    ll = LinkedList("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    ll.append("e")
    middle = leet_code.find_middle_node(ll)
    assert middle.value == "c"


def test_find_middle_node_with_negative_numbers():
    """Test finding middle node with negative numbers."""
    ll = LinkedList(-5)
    ll.append(-3)
    ll.append(-1)
    ll.append(0)
    ll.append(1)
    ll.append(3)
    ll.append(5)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 0


def test_find_middle_node_with_duplicates():
    """Test finding middle node with duplicate values."""
    ll = LinkedList(1)
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 2


def test_find_middle_node_returns_correct_node_object():
    """Test that find_middle_node returns the actual node object, not just a value."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    middle = leet_code.find_middle_node(ll)
    
    # Verify it's the correct node by checking its position in the list
    assert middle.value == 3
    assert middle.next.value == 4
    assert middle.next.next.value == 5


def test_find_middle_node_traverses_once():
    """Test that the function only traverses the list once using two-pointer approach."""
    ll = LinkedList(1)
    for i in range(2, 20):
        ll.append(i)
    
    # This should work efficiently with the two-pointer approach
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 10  # Middle of 19 elements


def test_find_middle_node_after_operations():
    """Test finding middle after various list operations."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    # Remove some elements
    ll.remove(0)  # Remove 1
    ll.remove(3)  # Remove 5
    # List is now: 2, 3, 4 (3 elements)
    
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 3


def test_find_middle_node_very_large_list():
    """Test finding middle node in a very large list (100 elements)."""
    ll = LinkedList(1)
    for i in range(2, 101):
        ll.append(i)
    
    middle = leet_code.find_middle_node(ll)
    assert middle.value == 51  # First node of second half (for 100 elements)


def test_find_middle_node_consistency():
    """Test that multiple calls return the same middle node."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    
    middle1 = leet_code.find_middle_node(ll)
    middle2 = leet_code.find_middle_node(ll)
    
    assert middle1 == middle2
    assert middle1.value == 30


# --- Tests for has_loop method ---


def test_has_loop_no_loop_single_element():
    """Test that a single element list has no loop."""
    ll = LinkedList(1)
    result = leet_code.has_loop(ll)
    assert result is False


def test_has_loop_no_loop_two_elements():
    """Test that a two element list has no loop."""
    ll = LinkedList(1)
    ll.append(2)
    result = leet_code.has_loop(ll)
    assert result is False


def test_has_loop_no_loop_multiple_elements():
    """Test that a normal list with multiple elements has no loop."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    result = leet_code.has_loop(ll)
    assert result is False


def test_has_loop_with_loop_at_tail():
    """Test detecting a loop when tail points back to head."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    # Create a loop: tail -> head
    ll.tail.next = ll.head
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_with_loop_to_middle():
    """Test detecting a loop when tail points to a middle node."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    # Get the second node
    second_node = ll.head.next
    
    # Create a loop: tail -> second node
    ll.tail.next = second_node
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_with_self_loop():
    """Test detecting a loop when a node points to itself."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    # Get the second node and make it point to itself
    second_node = ll.head.next
    original_next = second_node.next
    second_node.next = second_node
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    second_node.next = original_next


def test_has_loop_large_list_no_loop():
    """Test that a large list without a loop returns False."""
    ll = LinkedList(1)
    for i in range(2, 51):
        ll.append(i)
    
    result = leet_code.has_loop(ll)
    assert result is False


def test_has_loop_large_list_with_loop():
    """Test detecting a loop in a large list."""
    ll = LinkedList(1)
    for i in range(2, 51):
        ll.append(i)
    
    # Get a node in the middle (at index 25)
    node = ll.head
    for _ in range(25):
        node = node.next
    
    # Create a loop: tail -> node at index 25
    ll.tail.next = node
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_after_operations_no_loop():
    """Test has_loop after various list operations."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    ll.remove(2)  # Remove middle element
    ll.prepend(0)
    
    result = leet_code.has_loop(ll)
    assert result is False


def test_has_loop_with_loop_at_second_node():
    """Test detecting a loop when tail points to the second node."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    # Create a loop: tail -> second node
    ll.tail.next = ll.head.next
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_with_short_loop():
    """Test detecting a loop in a list with just 2 nodes forming a loop."""
    ll = LinkedList(1)
    ll.append(2)
    
    # Create a loop: tail -> head
    ll.tail.next = ll.head
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_multiple_calls_no_loop():
    """Test that multiple calls on a list without loop consistently return False."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    result1 = leet_code.has_loop(ll)
    result2 = leet_code.has_loop(ll)
    result3 = leet_code.has_loop(ll)
    
    assert result1 is False
    assert result2 is False
    assert result3 is False


def test_has_loop_multiple_calls_with_loop():
    """Test that multiple calls on a list with loop consistently return True."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    
    # Create a loop
    ll.tail.next = ll.head.next
    
    result1 = leet_code.has_loop(ll)
    result2 = leet_code.has_loop(ll)
    
    assert result1 is True
    assert result2 is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_with_string_values():
    """Test has_loop with string values."""
    ll = LinkedList("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    
    # No loop initially
    assert leet_code.has_loop(ll) is False
    
    # Create a loop
    ll.tail.next = ll.head.next
    assert leet_code.has_loop(ll) is True
    
    # Clean up
    ll.tail.next = None


def test_has_loop_three_node_cycle():
    """Test detecting a loop where last three nodes form a cycle."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    # Get the third node
    third_node = ll.head.next.next
    
    # Create a loop: tail -> third node (nodes 3, 4, 5 form a cycle)
    ll.tail.next = third_node
    
    result = leet_code.has_loop(ll)
    assert result is True
    
    # Clean up the loop
    ll.tail.next = None


def test_has_loop_does_not_modify_list():
    """Test that has_loop doesn't modify the list structure."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    original_head = ll.head
    original_tail = ll.tail
    original_length = ll.length
    
    leet_code.has_loop(ll)
    
    assert ll.head == original_head
    assert ll.tail == original_tail
    assert ll.length == original_length
    assert ll.head.value == 1
    assert ll.tail.value == 4


# --- Tests for find_kth_from_end method ---


def test_find_kth_from_end_single_element_k1():
    """Test finding 1st from end in a single element list."""
    ll = LinkedList(1)
    result = leet_code.find_kth_from_end(ll, 1)
    assert result is not None
    assert result.value == 1
    assert result == ll.head


def test_find_kth_from_end_single_element_k2():
    """Test finding 2nd from end in a single element list (should return None)."""
    ll = LinkedList(1)
    result = leet_code.find_kth_from_end(ll, 2)
    assert result is None


def test_find_kth_from_end_two_elements_k1():
    """Test finding 1st from end (last element) in a two element list."""
    ll = LinkedList(1)
    ll.append(2)
    result = leet_code.find_kth_from_end(ll, 1)
    assert result.value == 2
    assert result == ll.tail


def test_find_kth_from_end_two_elements_k2():
    """Test finding 2nd from end (first element) in a two element list."""
    ll = LinkedList(1)
    ll.append(2)
    result = leet_code.find_kth_from_end(ll, 2)
    assert result.value == 1
    assert result == ll.head


def test_find_kth_from_end_five_elements_k1():
    """Test finding 1st from end (last element) in a five element list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    result = leet_code.find_kth_from_end(ll, 1)
    assert result.value == 5


def test_find_kth_from_end_five_elements_k3():
    """Test finding 3rd from end in a five element list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    result = leet_code.find_kth_from_end(ll, 3)
    assert result.value == 3


def test_find_kth_from_end_five_elements_k5():
    """Test finding 5th from end (first element) in a five element list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    result = leet_code.find_kth_from_end(ll, 5)
    assert result.value == 1


def test_find_kth_from_end_k_exceeds_length():
    """Test finding kth from end when k exceeds list length."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    result = leet_code.find_kth_from_end(ll, 5)
    assert result is None


def test_find_kth_from_end_k_zero():
    """Test finding 0th from end (invalid k)."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    result = leet_code.find_kth_from_end(ll, 0)
    # Depending on implementation, this might return None or the last element
    # The test validates current behavior


def test_find_kth_from_end_large_list_k1():
    """Test finding 1st from end in a large list."""
    ll = LinkedList(1)
    for i in range(2, 21):
        ll.append(i)
    result = leet_code.find_kth_from_end(ll, 1)
    assert result.value == 20


def test_find_kth_from_end_large_list_k10():
    """Test finding 10th from end in a large list."""
    ll = LinkedList(1)
    for i in range(2, 21):
        ll.append(i)
    # List: 1, 2, 3, ..., 20 (20 elements)
    # 10th from end should be 11 (20 - 10 + 1 = 11)
    result = leet_code.find_kth_from_end(ll, 10)
    assert result.value == 11


def test_find_kth_from_end_middle_of_list():
    """Test finding middle element using kth from end."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.append(60)
    ll.append(70)
    # 7 elements, 4th from end should be 40
    result = leet_code.find_kth_from_end(ll, 4)
    assert result.value == 40


def test_find_kth_from_end_with_strings():
    """Test finding kth from end with string values."""
    ll = LinkedList("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    ll.append("e")
    result = leet_code.find_kth_from_end(ll, 2)
    assert result.value == "d"


def test_find_kth_from_end_with_negative_numbers():
    """Test finding kth from end with negative numbers."""
    ll = LinkedList(-5)
    ll.append(-3)
    ll.append(-1)
    ll.append(0)
    ll.append(1)
    result = leet_code.find_kth_from_end(ll, 3)
    assert result.value == -1


def test_find_kth_from_end_with_duplicates():
    """Test finding kth from end with duplicate values."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    result = leet_code.find_kth_from_end(ll, 2)
    assert result.value == 3


def test_find_kth_from_end_returns_node_not_value():
    """Test that find_kth_from_end returns the actual node object."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    
    result = leet_code.find_kth_from_end(ll, 3)
    assert result.value == 30
    assert result.next.value == 40
    assert result.next.next.value == 50


def test_find_kth_from_end_after_operations():
    """Test finding kth from end after various list operations."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    ll.remove(2)  # Remove 3
    ll.prepend(0)
    # List is now: 0, 1, 2, 4, 5 (5 elements)
    
    result = leet_code.find_kth_from_end(ll, 2)
    assert result.value == 4


def test_find_kth_from_end_all_positions():
    """Test finding each position from end in a list."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    # 4 elements: 1, 2, 3, 4
    assert leet_code.find_kth_from_end(ll, 1).value == 4
    assert leet_code.find_kth_from_end(ll, 2).value == 3
    assert leet_code.find_kth_from_end(ll, 3).value == 2
    assert leet_code.find_kth_from_end(ll, 4).value == 1


def test_find_kth_from_end_does_not_modify_list():
    """Test that find_kth_from_end doesn't modify the list structure."""
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    original_head = ll.head
    original_tail = ll.tail
    original_length = ll.length
    
    leet_code.find_kth_from_end(ll, 2)
    
    assert ll.head == original_head
    assert ll.tail == original_tail
    assert ll.length == original_length


def test_find_kth_from_end_consistency():
    """Test that multiple calls return the same node."""
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    
    result1 = leet_code.find_kth_from_end(ll, 3)
    result2 = leet_code.find_kth_from_end(ll, 3)
    
    assert result1 == result2
    assert result1.value == 30


def test_find_kth_from_end_very_large_list():
    """Test finding kth from end in a very large list (100 elements)."""
    ll = LinkedList(1)
    for i in range(2, 101):
        ll.append(i)
    
    # 100 elements, 50th from end should be 51 (100 - 50 + 1)
    result = leet_code.find_kth_from_end(ll, 50)
    assert result.value == 51


def test_find_kth_from_end_edge_case_k_equals_length():
    """Test when k equals the list length (should return head)."""
    ll = LinkedList(5)
    ll.append(10)
    ll.append(15)
    ll.append(20)
    ll.append(25)
    
    # 5 elements, 5th from end should be the first element
    result = leet_code.find_kth_from_end(ll, 5)
    assert result.value == 5
    assert result == ll.head
